import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import speech_recognition as sr
import os

# Suppress warnings from ALSA/JACK
os.environ["PYTHONWARNINGS"] = "ignore::UserWarning"

class VoiceControlTurtlesim(Node):
    def __init__(self):
        super().__init__('voice_control_node')
        # Publisher to send movement commands to turtlesim
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.get_logger().info("Voice control node started.")

        # Start the voice control loop
        self.voice_control_loop()

    def voice_control_loop(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        while rclpy.ok():
            try:
                with microphone as source:
                    self.get_logger().info("Listening for command... Say 'forward', 'backward', 'left', 'right'.")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Set timeouts to avoid hanging

                # Recognize the command from audio input
                command = recognizer.recognize_google(audio).lower()
                self.get_logger().info(f"Command received: {command}")
                self.execute_command(command)

            except sr.UnknownValueError:
                self.get_logger().warning("Could not understand the command.")
            except sr.RequestError as e:
                self.get_logger().error(f"Speech recognition error: {e}")
            except Exception as e:
                self.get_logger().error(f"Error during voice recognition: {e}")

    def execute_command(self, command):
        twist = Twist()

        if 'forward' in command:
            twist.linear.x = 2.0
        elif 'backward' in command:
            twist.linear.x = -2.0
        elif 'left' in command:
            twist.angular.z = 2.0
        elif 'right' in command:
            twist.angular.z = -2.0
        else:
            self.get_logger().warning("Unknown command. Say 'forward', 'backward', 'left', or 'right'.")
            return

        # Publish the command to turtlesim
        self.publisher.publish(twist)
        self.get_logger().info(f"Executed command: {command}")

def main():
    rclpy.init()
    node = VoiceControlTurtlesim()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
