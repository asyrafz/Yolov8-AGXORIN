import subprocess
import time
import psutil
import os

def kill_process_on_port(port):
    for conn in psutil.net_connections():
        if conn.laddr.port == port:
            try:
                process = psutil.Process(conn.pid)
                process.terminate()
                process.wait(timeout=5)
                print(f"Process on port {port} terminated.")
                return True
            except psutil.NoSuchProcess:
                print(f"Process on port {port} not found.")
            except psutil.TimeoutExpired:
                print(f"Timeout while terminating process on port {port}.")
    print(f"No process found on port {port}.")
    return False

def reset_camera():
    camera_devices = [d for d in os.listdir('/dev') if d.startswith('video')]
    for device in camera_devices:
        device_path = f"/dev/{device}"
        try:
            os.system(f"sudo rmmod uvcvideo")
            time.sleep(1)
            os.system(f"sudo modprobe uvcvideo")
            print(f"Reset camera device: {device_path}")
        except Exception as e:
            print(f"Error resetting camera device {device_path}: {str(e)}")

def main():
    # ROS bridge typically uses port 9090
    ros_bridge_port = 9090

    print("Attempting to reset ROS bridge port...")
    if kill_process_on_port(ros_bridge_port):
        print(f"Waiting for port {ros_bridge_port} to be fully released...")
        time.sleep(5)
    else:
        print(f"No process was using port {ros_bridge_port}")

    print("\nAttempting to reset camera...")
    reset_camera()

    print("\nReset process completed. You can now try running your ROS bridge and camera again.")

if __name__ == "__main__":
    main()
