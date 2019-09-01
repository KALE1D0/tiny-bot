from none import on_command, NoneBot 
import config
import psutil
import sys
import os

@on_command('reboot', aliases=('系统重载',), only_to_me=False)
async def ai_restart(session):
	if (session.ctx['user_id'] in config.SUPERUSERS):
		await session.send("收到！所有模块重新载入中……")
		restart_program()
	else:
		await session.send("很抱歉，您无此权限，请联系理事长处理。")

def restart_program():
	p = psutil.Process(os.getpid())
	for handler in p.open_files() + p.connections():
		os.close(handler.fd)
	python = sys.executable
	os.execl(python, python, * sys.argv)
	