from none import on_command, NoneBot, MessageSegment
import subprocess
import random
import string
import config
import sys
import os
from utils.image import draw_image

@on_command('status', aliases=("状态",), only_to_me=False)
async def status(session):
	ret = subprocess.getoutput('nvidia-smi')
	fn = ''.join(random.sample(string.ascii_letters + string.digits, 16)) + '.png'
	draw_image(ret, os.path.join('..','data','image',fn))
	await session.send("[CQ:image,file=" + fn + "]")

