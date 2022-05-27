import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        initpose = PoseWithCovarianceStamped()
        initpose.header.frame_id = 'map'
        initpose.pose.pose.position.x = 0.0
        initpose.pose.pose.position.y = 0.0
        initpose.pose.pose.position.z = 0.0

        
        
        initpose.pose.pose.orientation.x = 0.0
        initpose.pose.pose.orientation.y = 0.0
        initpose.pose.pose.orientation.z = 0.0
        initpose.pose.pose.orientation.w = 1.0
        self.publisher_.publish(initpose)
        # self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1
        self.timer.cancel()




def main(args=None):
    # print('Hi from my_package.')
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
