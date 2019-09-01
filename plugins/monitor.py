from none import on_command, NoneBot, MessageSegment
import subprocess
import random
import string
import config
import sys
import os
import re
from utils.image import draw_image

@on_command('monitor', aliases=("性能",), only_to_me=False)
async def monitor(session):
	ret = subprocess.getoutput('top -b -n1')
	fn = ''.join(random.sample(string.ascii_letters + string.digits, 16)) + '.png'
	draw_image(ret, os.path.join('..','data','image',fn))
	await session.send("[CQ:image,file=" + fn + "]")
