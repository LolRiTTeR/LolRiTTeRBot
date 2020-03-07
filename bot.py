# oompa loompa modafukka

import json
import traceback
import time
from discord.ext import commands
import discord


class RitterBot(commands.AutoShardedBot):
	def __init__(self, **options):
		with open('./data/config.json', 'r') as f:
			self.config = json.load(f)  # type: dict
		with open('./data/token.json', 'r') as f:
			self.token = json.load(f)  # type: dict
		self.login_errors = []
		self.initial_extensions = [
			'main',
			'errors',
			'help',
			'stats'
		]

		super().__init__(
			command_prefix=self.config['prefix'],
			activity=discord.Game(name=self.config['startup_status']), **options
		)

	def load(self, *extensions):
		for cog in extensions:
			try:
				self.load_extension(f"cogs.{cog}")
				print(f"Loaded {cog}")
			except commands.ExtensionNotFound:
				print(f"Couldn't find {cog}")
			except commands.ExtensionError:
				self.login_errors.append(f"Ignoring exception in Cog: {cog}\n{traceback.format_exc()}")
		print("Loaded extensions")

	def load_initial_extensions(self):
		for cog in self.initial_extensions:
			try:
				self.load_extension(f"cogs.{cog}")
				print(f"Loaded {cog}")
			except commands.ExtensionNotFound:
				print(f"Couldn't find {cog}")
			except commands.ExtensionError:
				self.login_errors.append(f"Ignoring exception in Cog: {cog}\n{traceback.format_exc()}")



	def run(self):
		self.load_initial_extensions()
		super().run(self.token["token"])


bot = RitterBot(max_messages=10000)

if not bot.config['use_default_help']:
	bot.remove_command('help')

@bot.event
async def on_ready():
	print('------------')
	print('Logged in as')
	print(bot.user)
	print(bot.user.id)
	print('------------')
	for error in bot.login_errors:
		print(error)


try:
	bot.run()
except discord.errors.LoginFailure:
	print("Invalid login token")
except KeyboardInterrupt:
	print("You think you can just ctrl+c to get away you little bitch?")
	time.sleep(1)
	print("I know where you live cunt")
	time.sleep(5)
