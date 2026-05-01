# 机器人全链路系统 (Full-Stack Robotics System)
> **使用说明**：在VS Code中打开此Markdown文件，按 `Ctrl+Shift+O`（Windows/Linux）或 `Cmd+Shift+O`（Mac）即可调出大纲面板，或点击左侧活动栏的「大纲」图标查看完整树状结构。

## 一、感知层（传感器系统 - Perception Layer）
### 1.1 环境感知 (Exteroception)
#### 1.1.1 视觉类 (Vision)
- 单目相机 (Monocular Camera)
- 双目相机 (Stereo Camera)
- 深度相机 (RGB-D Camera，如 Kinect、Realsense)
- 激光雷达 (LiDAR - 2D/3D)
- 红外相机 (IR Camera)
#### 1.1.2 距离与测距 (Proximity & Ranging)
- 超声波传感器 (Ultrasonic)
- 飞行时间传感器 (ToF - Time of Flight)
- 红外测距 (IR Ranging)
#### 1.1.3 环境状态 (Environmental)
- 温湿度传感器
- 气压/高度计 (Barometer)
- 气体传感器

### 1.2 本体感知 (Proprioception)
#### 1.2.1 运动学状态 (Kinematics)
- 编码器 (Encoder：增量式 Incremental、绝对式 Absolute)
- 惯性测量单元 (IMU)
- 陀螺仪 (Gyroscope)
- 加速度计 (Accelerometer)
#### 1.2.2 动力学状态 (Dynamics)
- 六维力矩传感器 (6-Axis F/T Sensor - 人形机器人足端与腕部核心)
- 一维张力/拉压传感器
- 触觉传感器 (Tactile Sensor / 电子皮肤)
#### 1.2.3 全局定位 (Localization)
- RTK-GPS / GNSS
- UWB 室内定位系统
- 磁力计/电子罗盘 (Magnetometer)

### 1.3 特殊与交互传感器
#### 1.3.1 语音与声学
- 麦克风阵列 (Mic Array - 大模型语音交互必备)
#### 1.3.2 离散接触类
- 防撞边 / 触边开关 (Bumper)
- 机械限位开关 (Limit Switch)

### 1.4 数据预处理与同步 (Data Pipeline & Synchronization)
- **时钟同步 (Time Synchronization)**：PTP (精确时间协议), NTP (多传感器数据对齐前提)
- **系统标定 (Calibration)**：相机内参标定、手眼标定 (Hand-Eye Calibration)、多传感器联合外参标定

---

## 二、决策层（上位机系统 / “大脑” - High-level Decision System）
> **架构演进说明**：上位机负责“想干什么”。在小车中通常负责导航建图；在具身智能/人形机器人中，升级为处理多模态大模型和高级任务规划的“大脑皮层”。

### 2.1 计算硬件平台演进 (Computing Hardware)
#### 2.1.1 经典上位机 (适用于小车/轻量级机器人)
- 单板计算机 (SBC)：树莓派 (Raspberry Pi)、Rockchip RK3588等
- 低功耗边缘计算盒
#### 2.1.2 大算力上位机 (适用于人形/具身智能机器人头部)
- Nvidia Jetson 高级系列 (AGX Orin)
- x86 高性能迷你主机 (如 Intel NUC i7/i9)
- 标准工作站 / 独立显卡平台 (用于本地大模型推理)
#### 2.1.3 硬件加速单元
- FPGA 开发板
- AI NPU/TPU 算力棒

### 2.2 操作系统与运行环境 (OS & Middleware)
#### 2.2.1 通用操作系统 (GPOS)
- Ubuntu / Debian (Linux 核心，非强实时要求)
- Yocto (定制化嵌入式 Linux)
#### 2.2.2 机器人中间件 (Middleware) 👉 [跳转：ROS通信原理详解](./robotics/ros_communication.md)
- ROS 2 (Humble / Iron - DDS通信机制)
- ROS 1 (Noetic - 主从节点机制)

### 2.3 核心算法功能 (Core Algorithms)
#### 2.3.1 具身智能与智能控制 (Embodied AI & Control)
- 多模态大模型推理 (VLM/LLM 联网搜索与视觉推理)
- 模仿学习 (Imitation Learning) 与 强化学习 (Reinforcement Learning) 端到端控制
- 开放词汇目标检测 (Open-vocabulary Detection)
#### 2.3.2 导航与建图 (Navigation & Mapping)
- SLAM (同步定位与建图: 激光2D/3D, V-SLAM)
- 状态估计 (State Estimation / 滤波融合)
#### 2.3.3 高级规划与决策 (Planning)
- 全局路径规划 (Global Routing)
- 行为树决策 (Behavior Trees) / 状态机 (State Machine)
- 任务级指令拆解 (Task-level Decomposition)

### 2.4 人机交互系统 (Human-Robot Interaction - HRI)
- **显式交互 (Explicit)**：语音指令输入、AR/VR 遥操作 (Teleoperation)、手柄/摇杆控制、UI/Web 监控界面
- **隐式交互 (Implicit)**：人体意图预测 (Human Intention Prediction)、手势识别、目光/头部姿态跟随

---

## 三、控制层（下位机系统 / “小脑” - Low-level Motion Control System）
> **架构演进说明**：下位机负责“怎么做到”。在小车中是一块跑PID的单片机；在人形机器人中，由于算力需求呈指数级爆炸，下位机进化为一台运行强实时系统的PC主机，而原先的单片机被下放到关节驱动器中。

### 3.1 控制硬件平台演进 (Control Boards)
#### 3.1.1 经典单片机架构 (适用于小车/普通轮式底盘)
- ARM Cortex-M 系列微控制器 (STM32 等)
- ESP32 (带无线功能)
- Arduino (AVR)
#### 3.1.2 高性能PC级架构 (适用于人形/多足机器人胸部)
- **高性能 x86 主机 (如胸部 NUC)**：作为机器人整体姿态控制的小脑，充当 ROS Master。
- 工业 PLC / 专用多轴运动控制卡
#### 3.1.3 定制化底板 (Carrier Boards)
- 传感器接口板 / 信号隔离板
- 电源分配与控制一体板

### 3.2 操作系统与通信层 (OS & Communication)
#### 3.2.1 实时操作系统 (RTOS / 硬实时)
- RT-Preempt (带有实时补丁的 Linux 内核，人形机器人必备)
- FreeRTOS / RT-Thread (MCU常用)
- VxWorks
#### 3.2.2 高速总线主站 (Bus Master)
- EtherCAT 主站 (高频下发控制指令到全身几十个关节)
- CAN / CAN FD 主站

### 3.3 核心逻辑与算法 (Core Logic)
#### 3.3.1 经典闭环控制 (针对简单平台)
- 独立关节 PID 控制律
- 底盘运动学逆解算 (如差速、全向轮解算)
- 里程计推算 (Odometry Calculation)
#### 3.3.2 高阶动力学与平衡控制 (针对人形/足式等复杂平台)
- 全身控制算法 (WBC - Whole-Body Control)
- 复杂运动学逆解 (IK - Inverse Kinematics，如14自由度双臂逆解)
- 模型预测控制 (MPC - Model Predictive Control)
- 质心运动学规划 / 零矩点 (ZMP) 动态平衡维持

---

## 四、执行层（执行器系统 / “神经末梢与肌肉” - Actuator System）
### 4.1 动力与驱动核心 (Power & Drive)
- **4.1.1 关节级微控制器 (内嵌 MCU)**
    - 每个电机自带的微型伺服驱动板，负责接收高频指令并执行底层闭环。
- **4.1.2 驱动控制算法**
    - 矢量控制 (FOC - Field Oriented Control) —— *心脏算法，高频电流闭环*
    - 方波控制 (Trapezoidal / 六步换相)
    - 步进脉冲控制
- **4.1.3 功率变换电路 (Power Electronics)**
    - MOSFET/IGBT 逆变桥 (Inverter Bridge)
    - 预驱动电路 (Gate Driver)

### 4.2 运动执行器 (Motion Actuators)
#### 4.2.1 旋转类 (Rotary)
- 高扭矩无框力矩电机 (Frameless Motor - 人形关节主流)
- 直流无刷电机 (BLDC) / 永磁同步电机 (PMSM)
- 伺服电机系统 (Servo System)
#### 4.2.2 直线与流体类 (Linear & Fluid)
- 直线电机 (Linear Motor)
- 电动推杆 (Linear Actuator) / 滚珠丝杠模组
- 气缸 (Pneumatic Cylinder) 与 气动肌肉 (PAM)

### 4.3 传动与关节模组 (Transmission & Joints)
#### 4.3.1 精密减速器 (Precision Reducers)
- 谐波减速器 (Harmonic Drive) —— *机械臂/双足高精轻量化传动*
- RV 减速器 (Rotary Vector) —— *高负载传动*
- 行星减速器 (Planetary Gearbox) —— *机器狗关节常用*
#### 4.3.2 一体化关节 (Actuator Module)
- 减速器+电机+编码器+驱动板高度集成模块 (如准直驱关节 / 串联弹性驱动器 SEA)
#### 4.3.3 关节安全与制动装置 (Safety & Braking)
- 电磁抱闸 (Electromagnetic Brake - 断电锁死保护)
- 机械限位挡块 (Mechanical Stop)

### 4.4 操作与末端执行器 (Manipulators)
- 灵巧手 (Dexterous Hand - 多指独立驱动)
- 机械平行夹爪 (Parallel Gripper)
- 柔性抓取器 (Soft Gripper)
- 真空吸盘 (Vacuum Cup)

### 4.5 辅助执行器 (Auxiliary)
- 声光指示 (LED / 蜂鸣器 Buzzer)
- 继电器 (Relay) / 电磁阀 (Solenoid Valve)

---

## 五、机械结构层 (Mechanical Structure Layer)
### 5.1 承载主体 (Chassis & Frame)
#### 5.1.1 移动形态 (Mobile Chassis)
- 轮式 (差速 Differential、全向 Omni/Mecanum)
- 履带式 (Tracked)
- 腿式 (单足、双足人形 Bipedal、四足狗 Quadruped)
#### 5.1.2 骨架与外壳 (Frame & Shell)
- 航空级铝合金切削件 / 碳纤维框架 (轻量化高刚度需求)
- 3D 打印 / 注塑 / 玻璃钢外壳

### 5.2 宏观传动机构 (Macro Transmission)
- 同步带传动 (Timing Belt)
- 齿轮齿条 (Gear & Rack)
- 连杆机构 (Linkage Mechanism - 四足/双足腿部常见)
- 钢丝绳传动 (Tendon-driven - 灵巧手常用)

### 5.3 结构辅助件 (Hardware Fasteners)
- 精密轴承 (交叉滚子轴承、角接触轴承)
- 联轴器 (Couplings)
- 减震器 (Shock Absorbers / 阻尼器)

---

## 六、系统安全与防护机制 (Safety & Security)
> **说明**：贯穿全身软硬件的底层红线，确保机器人与人类环境交互时的绝对物理与网络安全。

### 6.1 软件与控制层安全 (Software & Control Safety)
- 看门狗定时器 (Watchdog Timer - 死机自动重启/锁死保护)
- 异常状态机 (Fault State Machine - 故障分级响应与紧急停止)
- 碰撞检测与柔顺控制 (Collision Detection & Compliance - 遇到异常阻力自动变软)
- 关节软限位 (Software Joint Limits - 动态限制最大角度/速度/力矩)

### 6.2 网络与通信安全 (Cybersecurity)
- ROS 2 SROS/DDS 加密与访问控制机制 (防止控制节点被恶意劫持)
- 局域网隔离与高频控制网络防火墙策略

---

## 七、通信系统 (Communication System)
### 7.1 内部总线与网络 (Internal Bus)
#### 7.1.1 高速硬实时总线 (小脑与全身关节通信)
- EtherCAT (微秒级同步，支持星型/链型拓扑)
- CAN / CAN FD 总线 (毫秒级同步)
#### 7.1.2 板级与外设通信 (Board-Level)
- UART (串口) / USB / SPI / I2C / I3S
#### 7.1.3 大脑与小脑通信网络 (Upper to Lower)
- 千兆/万兆以太网 (Gigabit Ethernet，TCP/UDP)

### 7.2 外部遥测与交互 (Telemetry & External)
- Wi-Fi (局域网SSH调试 / ROS主从机无线外链)
- Bluetooth (蓝牙手柄接入)
- 4G/5G 蜂窝网络 (云端大脑/大模型API远程接入)

---

## 八、电源系统 (Power System)
### 8.1 能源储备 (Energy Storage)
- 高倍率动力锂电池组 (Li-ion/LiPo Pack - 满足人形机器人瞬间爆发大电流)
- 超级电容 (Supercapacitor - 瞬时动态充放电补偿)
- 电池热管理系统 (液冷/风冷散热结构)

### 8.2 电池管理系统 (BMS - Battery Management System)
- 电芯均衡控制 (Cell Balancing) / 充放电保护
- 智能电量计 (SOC / SOH 状态高精度估算与实时上报)

### 8.3 电源转换与分配 (Power Distribution)
- PDU (高频开关电源分配单元 Power Distribution Unit)
- 多路 DC-DC 降压模块 (48V/24V转12V/5V/3.3V) / 升压模块
- 急停开关 (E-Stop - 物理切断高压动力电，保留低压逻辑电) 与 快熔断器 (Fuse)

---

## 九、开发与仿真环境 (Development & Toolchain)
> **说明**：支持算法迭代、虚拟训练与工程部署的基础设施（DevOps）。

### 9.1 物理仿真器 (Simulators)
- MuJoCo (强动力学仿真，强化学习训练主流)
- Isaac Sim (Nvidia 推出，强逼真渲染与 GPU 并行加速)
- Gazebo / Webots (ROS 生态经典开源仿真平台)

### 9.2 调试与可视化工具 (Debugging Tools)
- RViz (ROS 原生三维空间可视化工具)
- rqt / PlotJuggler (传感器与控制参数实时数据曲线绘制)
- Foxglove Studio (现代机器人全功能、跨平台调试仪表盘)

### 9.3 部署与版本控制 (CI/CD)
- Docker / 容器化部署 (隔离运行环境，保证上下位机部署一致性)
- Git / GitHub / GitLab (代码版本与协作控制)  👉 [跳转：git/github笔记](./robotics/git_github.md)
- 自动化测试管道 (Automated Testing Pipelines - 代码合并前的单元测试与仿真验证)