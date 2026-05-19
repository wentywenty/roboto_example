#!/usr/bin/env python3
# -*- coding: encoding -*-

# Copyright (C) 2026 Luo1imasi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import imu_py
import time

def example_serial_imu():
    """使用串口连接的IMU示例"""
    print("=== 串口IMU示例 ===")
    try:
        imu = imu_py.IMUDriver.create_imu(
            imu_id=8,
            interface_type="serial",
            interface="/dev/ttyUSB0",
            imu_type="HIPNUC",
            baudrate=921600
        )
    except Exception as e:
        print(f"创建IMU失败: {e}")
        return
    
    print(f"IMU ID: {imu.get_imu_id()}")
    
    for i in range(1000):
        quat = imu.get_quat()
        print(f"四元数: w={quat[0]:.4f}, x={quat[1]:.4f}, y={quat[2]:.4f}, z={quat[3]:.4f}")
        
        ang_vel = imu.get_ang_vel()
        print(f"角速度: x={ang_vel[0]:.4f}, y={ang_vel[1]:.4f}, z={ang_vel[2]:.4f} rad/s")
        
        lin_acc = imu.get_lin_acc()
        print(f"线加速度: x={lin_acc[0]:.4f}, y={lin_acc[1]:.4f}, z={lin_acc[2]:.4f} m/s^2")
        
        temp = imu.get_temperature()
        print(f"温度: {temp:.2f}°C")
        
        print("-" * 50)
        time.sleep(0.01)

if __name__ == "__main__":
    example_serial_imu()