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

import motors_py
import time

def example_can_motor():
    """使用CAN总线连接的电机示例"""
    print("=== CAN电机示例 ===")
    motors = []
    try:
        for i in range(1, 2):
            motors.append(motors_py.MotorDriver.create_motor(
            motor_id=i,
            interface_type="can",
            interface="can0",
            motor_type="DM",
            motor_model=0,
            master_id_offset=16,
        ))
        print("电机创建成功！")
    except Exception as e:
        print(f"创建电机失败: {e}")
        return
    
    try:
        print("使能电机...")
        for motor in motors:
            motor.init_motor()
        
        print("\n=== MIT模式控制示例 ===")
        motors[0].set_motor_control_mode(motors_py.MotorControlMode.MIT)
        
        target_pos = -0.5
        target_vel = 0.0
        kp = 5.0
        kd = 1.0
        torque = 0.0
        
        motors[0].motor_mit_cmd(target_pos, target_vel, kp, kd, torque)
            
        # 读取电机状态
        pos = motors[0].get_motor_pos()
        vel = motors[0].get_motor_spd()
        current = motors[0].get_motor_current()
        temp = motors[0].get_motor_temperature()
        error_id = motors[0].get_error_id()
        
        print(f"位置: {pos:.4f} rad, 速度: {vel:.4f} rad/s, "
              f"电流: {current:.4f} A, 温度: {temp:.2f}°C, 错误码: {error_id}")
        time.sleep(1)
    except Exception as e:
        print(f"电机控制过程中出错: {e}")
    finally:
        for motor in motors:
            print("失能电机...")
            motor.deinit_motor()


if __name__ == "__main__":
    example_can_motor()
