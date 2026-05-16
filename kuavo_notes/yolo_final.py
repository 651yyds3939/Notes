import rospy
import cv2
import message_filters
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from geometry_msgs.msg import PointStamped
from ultralytics import YOLO

# 1. 加载模型
model = YOLO('models/yolov8n.pt')
bridge = CvBridge()

def callback(rgb_msg, depth_msg):
    # 2. 图像转换
    cv_image = bridge.imgmsg_to_cv2(rgb_msg, "bgr8")
    depth_image = bridge.imgmsg_to_cv2(depth_msg, "16UC1")
    
    # 3. YOLO 推理
    results = model(cv_image, classes=[39]) # 假设 39 是 bottle/box
    
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # 4. 获取中心点像素坐标
            x1, y1, x2, y2 = box.xyxy[0]
            center_u, center_v = int((x1 + x2)/2), int((y1 + y2)/2)
            
            # 5. 获取深度值 (mm 转 m)
            z_depth = depth_image[center_v, center_u] / 1000.0 
            
            # 6. 像素坐标系 -> 相机坐标系 -> 机器人基坐标系(base_link)
            # (此处需结合相机内参 fx, fy, cx, cy 和 TF 树进行变换)
            # 最终计算出目标在 base_link 下的 target_x, target_y, target_z
            
            # 7. 发布目标坐标
            target_msg = PointStamped()
            target_msg.header.frame_id = "base_link"
            target_msg.point.x = target_x
            target_msg.point.y = target_y
            target_msg.point.z = target_z
            yolo_pub.publish(target_msg)

# 8. 话题时间同步订阅
rgb_sub = message_filters.Subscriber('/camera/color/image_raw', Image)
depth_sub = message_filters.Subscriber('/camera/depth/image_rect_raw', Image)
ts = message_filters.ApproximateTimeSynchronizer([rgb_sub, depth_sub], 10, 0.1)
ts.registerCallback(callback)