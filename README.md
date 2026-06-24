# Notes

个人笔记与工程文档仓库。

---

## 目录树

```
Notes/
├── README.md
├── robot_system.md              # 机器人系统思维导图
├── robot_system_photo.html      # 思维导图 HTML 版
│
├── kuavo_notes/                 # ★ Kuavo 4 Pro 二次开发文档（我们自己的实战笔记）
│   ├── *.md                     #   仿真、导航、视觉抓取、RL、大模型、VLA 等
│   ├── scripts/                 #   辅助脚本
│   └── 5功能案例/               #   乐聚官方案例（通用 / 综合 / 拓展 / 五代 / 轮臂）
│
├── robotics/                    # 机器人通用文档（与具体机型无关）
│   ├── *.md                     #   ROS、架构、动力学、C++、Git、Docker 等
│   ├── code/                    #   编程基础笔记
│   └── ros_code_template/       #   ROS1/ROS2 代码模板
│
└── ubuntu/                      # Ubuntu 系统通用文档
    └── *.md                     #   开发环境、终端工具、网络代理、磁盘清理等
```

---

## 各目录说明

**[`kuavo_notes/`](./kuavo_notes/)** — 乐聚 Kuavo 4 Pro 的二次开发工程文档，记录我们在实际项目中的调试过程与经验总结。入口：[`1.READEME.md`](./kuavo_notes/1.READEME.md)（仿真环境部署）。

**[`kuavo_notes/5功能案例/`](./kuavo_notes/5功能案例/)** — 乐聚官方提供的功能案例，非我们自写。索引：[`案例目录.md`](./kuavo_notes/5功能案例/案例目录.md)。

**[`robotics/`](./robotics/)** — 机器人领域的通用知识，适用于任何机器人项目，不绑定 Kuavo。

**[`ubuntu/`](./ubuntu/)** — Ubuntu /Linux 日常开发与运维笔记，与机器人无关。

**[`robot_system.md`](./robot_system.md)** — 机器人全链路系统的思维导图，在 VS Code 中打开后可通过大纲视图浏览层级结构。
