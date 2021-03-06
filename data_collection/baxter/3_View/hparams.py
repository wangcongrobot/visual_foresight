""" Hyperparameters for Large Scale Data Collection (LSDC) """

import os.path
from visual_mpc.policy.random.gaussian import GaussianPolicy
from visual_mpc.agent.general_agent import GeneralAgent
from visual_mpc.envs.robot_envs.autograsp_env import AutograspEnv
from visual_mpc.envs.robot_envs.util.topic_utils import IMTopic

BASE_DIR = '/'.join(str.split(__file__, '/')[:-1])
current_dir = os.path.dirname(os.path.realpath(__file__))


env_params = {
    'email_login_creds': '/home/server/catkin_ws/src/private_visual_foresight/visual_mpc/envs/robot_envs/email_cred_baxter.json',
    'camera_topics': [IMTopic('/camera1/usb_cam/image_raw'),IMTopic('/camera2/usb_cam/image_raw'),IMTopic('/camera3/usb_cam/image_raw')],
    # 'camera_topics': [IMTopic('/camera2/pg_16466237/image_raw')],
    'robot_type': 'baxter',
    'gripper_attached': 'baxter_gripper',
    'print_debug': True,
    'OFFSET_TOL': 0.5

}

agent = {
    'type': GeneralAgent,
    'env': (AutograspEnv, env_params),
    'data_save_dir': BASE_DIR,
    'T': 30,
    'image_height' : 240,
    'image_width' : 320,
    'record': BASE_DIR + '/record/',
}


policy = {
    'type': GaussianPolicy,
    'nactions': 30,
    'repeat': 1,
    'initial_std': 0.035,   #std dev. in xy
    'initial_std_lift': 0.08,   #std dev. in z
}


config = {
    'traj_per_file':128,
    'current_dir' : current_dir,
    'save_data': True,
    'save_raw_images': True,
    'start_index':0,
    'end_index': 120000,
    'agent': agent,
    'policy': policy,
    'ngroup': 1000
}
