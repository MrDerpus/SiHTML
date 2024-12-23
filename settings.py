
class COMMENTS:
	SINGLE_LINE_SCRIPT:str = '//'
	SINGLE_LINE_HTML:str   = '--'

	MULTI_LINE_SCRIPT_START:str = '-*'
	MULTI_LINE_SCRIPT_END:str   = '*-'

	MULTI_LINE_HTML_START:str   = '/*'
	MULTI_LINE_HTML_END:str     = '*/'




class SYNTAX: # syntax settings that users can change.
	SEPARATOR:str = '|'
	CLOSE:str     = '~;' # Squiggle, used to close tags in defined in HTML_NON_INTERVENTION.

	CLASS:str = '.'
	ID:str    = '#'
	TAG_ATTRIBUTE:str = '~%'

	FUNCTION:str = '@'
	VARIABLE:str = '$'

	CHILD:str = '>' # This is only used in lists.




class HASH: # Hashes, because it's very unlikely for a person to type in a full hash.
	NO_INPUT_FILE:str     = '509bb0bcae3e762ece6891ce4d34a841'
	NO_OUTPUT_FILE:str    = 'f4d6cc0dc0dd99d177b8253bf1e43c6f'
	NO_USER_INPUT:str     = '75e2c40ffa5b937511e96840b56a4a7a'
	NON_EXISTENT_FILE:str = '948861a776811a7fd34ae2e73ee2adee'

	IGNORE:str  = 'a2e843feab94ef623fea888f07c28696'

	COMMENT:str = 'f2cd320b55767434dd48d81b165ea956'
	MULTI_LINE_COMMENT_START:str = '741e8dedeff3fda6a9183224ad3eab44'
	MULTI_LINE_COMMENT_END:str   = '11672c1086f8b351a09d6bbcc8915e43'




class VALID: # Valid HTML tags and language commands.
	# HTML tags -----------
	# HTML tags that are self-closing. Example: <link rel="stylesheet" type="text/css" href="styles.css" />
	# Note: Tags like 'keygen', 'command', 'menuitem', and 'frame' have been removed as they are not supported in HTML5.
	HTML_SELF_CLOSING:list = [
		'area', 'base', 'br', 'col', 'embed',
		'hr', 'img', 'input', 'link', 'meta',
		'param', 'source', 'track', 'wbr'
	]
	
	# HTML tags that are not self-closing but need intervention.
	# Example: <div id="idName">
	HTML_NON_INTERVENTION:list = [
		'abbr', 'address', 'aside', 'article', 'blockquote',
		'button', 'caption', 'colgroup', 'dialog', 'details',
		'div', 'figure', 'figcaption', 'footer', 'header',
		'head', 'main', 'nav', 'span'
	]
	
	# HTML tags that are not self-closing and DON'T need intervention.
	# Example: <h1 id="idName">Hello World!</h1>
	HTML_INTERVENTION:list = [
		'a', 'caption', 'col', 'colgroup', 'form',
		'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
		'label', 'object', 'p', 'textarea', 'table',
		'tbody', 'td', 'tfoot', 'th', 'thead', 'tr',
		'title'
	]
	
	# Blocked HTML tags.
	# Removed non-standard tags like 'bold', 'underline', 'italic' and duplicates.
	HTML_BLOCKED:list = [
		'b', 'i', 'u', 's', 'style'
		'bold', 'italic', 'underline', 'strong'
	]
	
	# HTML_CUSTOM:dict = {'style':'<link rel="stylesheet" type="text/css" href="{innerText}" />', }
	# Tags that are customized in the main.py file
	HTML_CUSTOM:list = [
		'body', 'favicon', 'html', 'icon',
		'li', 'ol', 'ul',
		'script', 'stylesheet'
	]


	# All valid HTML tags. that are specified above.
	HTML:list = [i for i in HTML_SELF_CLOSING + HTML_NON_INTERVENTION + HTML_INTERVENTION + HTML_CUSTOM]
	# ---------------------
 

	# Valid language commands -----------
	COMMANDS:list = ['set', 'var', 'inject', 'exit']
	# -----------------------------------


	# Valid language syntax -------------
	SYNTAX:dict = {
		'SYNTAX.SEPARATOR':SYNTAX.SEPARATOR,
		'SYNTAX.CLOSE':SYNTAX.CLOSE,
		'SYNTAX.ID':SYNTAX.ID,
		'SYNTAX.CLASS':SYNTAX.CLASS,
		'SYNTAX.TAG_ATTRIBUTE':SYNTAX.TAG_ATTRIBUTE,
		'SYNTAX.FUNCTION':SYNTAX.FUNCTION,
		'SYNTAX.VARIABLE':SYNTAX.VARIABLE,
		'SYNTAX.CHILD':SYNTAX.CHILD 
	}
	# -----------------------------------
	
	VALID:list = [i for i in HTML + COMMANDS]