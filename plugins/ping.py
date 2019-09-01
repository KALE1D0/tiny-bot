from none import on_command, NoneBot 
import config
import sys
import os
@on_command('ai', aliases=("艾酱",), only_to_me=False)
async def ping(session):
	await session.send("咱在~")

@on_command('ping', aliases=("呯",), only_to_me=False)
async def ping(session):
	await session.send("啪！")
