import re

custom_color = {'reg': 'fg:#00ff00', 'hex_val': 'fg:#bbbbbb', 'cons': 'red'}

pattern = re.compile(
	r'(\b(?:[re]?[abcd][xh]|[re]?[sd]il?|[re]?[sb]pl?|[re]?dx|r[0-9]{1,2}[dbw]?)\b)|'
	r'(0x[0-9a-fA-F]+)|'
	r'\b(constraints)\b'
)

def format_part(text):
	result = []
	last_end = 0
	for match in pattern.finditer(text):
		if match.start() > last_end:
			result.append(('', text[last_end:match.start()]))
		reg, hex_val, cons = match.groups()
		if reg:
			result.append((custom_color['reg'], reg))
		elif hex_val:
			result.append((custom_color['hex_val'], hex_val))
		elif cons:
			result.append((custom_color['cons'], cons))
		last_end = match.end()
	if match.end() < len(text):
		result.append(('', text[last_end:]))
	return result

def format_one_gadget(one_gadget):
	output = []
	output.append((custom_color['hex_val'], hex(one_gadget['value'])))
	output.append(('', ' '))
	output.extend(format_part(one_gadget['effect']))
	output.append(('', '\n    '))
	output.append((custom_color['cons'], 'constraints'))
	output.append(('', ':\n'))
	constraints = one_gadget['constraints']
	for c in constraints:
		output.append(('', '        '))
		output.extend(format_part(c))
		output.append(('', '\n'))
	return output