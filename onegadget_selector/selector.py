import subprocess
from pwn import *
import json
import questionary
from questionary import Style, Choice

from .formatter import format_one_gadget

custom_style = Style([
    ('pointer', 'fg:#00ffff bold'),
])

def show_onegadgets(libc_path):
	cmd = ['one_gadget', libc_path]
	subprocess.run(cmd)

def select_onegadgets(libc_path):
	cmd = ['one_gadget', '-o', 'json', libc_path]
	one_gadgets = json.loads(subprocess.check_output(cmd).decode())
	if not one_gadgets:
		log.warning('One_Gadget Not Found!')
		return 0
	choices = [
    	Choice(title = format_one_gadget(g), value = g['value']) 
    	for g in one_gadgets
	]
	selected = questionary.select(
		'Choose a one_gadget:\n',
		qmark = '[*]',
		instruction = ' ',
		choices = choices,
		style = custom_style,
		pointer = '=>'
	).ask()
	return selected