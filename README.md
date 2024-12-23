![silogo](https://github.com/user-attachments/assets/75ae3909-1a7d-45d0-92c3-5d402f78d5af)


# SiHTML (Simple HTML) v2.4.0 - Alpha

### SiHTML is a custom programming language designed to streamline the process of creating webpages by offering a simplified syntax reminiscent of the popular EMMET plugin syntax found in various code editors. SiHTML aims to empower developers of all experience levels by eliminating the need for manually closing tags and ensuring correct tag order, thus enabling rapid webpage development without sacrificing flexibility or control.


## Key Features:
- **Simplified Syntax:** SiHTML employs a concise and intuitive syntax inspired by the EMMET plugin, allowing developers to write HTML markup quickly and efficiently. With SiHTML, developers can write markup in shorthand without worrying about closing tags or maintaining the correct tag order.

- **Automatic Tag Closure:** One of the standout features of SiHTML is its ability to close HTML tags automatically, sparing developers the need to close tags manually. SiHTML intelligently detects tag nesting and automatically inserts closing tags where necessary, reducing the likelihood of syntax errors and streamlining the coding process.

- **Intuitive Tag Nesting:** SiHTML encourages a clear and logical structure by enforcing intuitive tag nesting. Developers can easily create complex nested structures without needing to meticulous attention to detail, allowing for faster prototyping and development iterations.

- **Familiarity for EMMET Users:** SiHTML's syntax closely mirrors that of the EMMET plugin, making it instantly familiar to developers who are accustomed to using EMMET for code expansion and shorthand notation. This familiarity promotes rapid adoption and minimizes the learning curve for developers transitioning to SiHTML.

- **Accessibility and Versatility:** SiHTML is designed to be accessible to developers of all skill levels, from beginners to seasoned professionals. Its simplicity and flexibility make it well-suited for a wide range of web development projects, from simple landing pages to complex web applications.

- **Variable Declaration:** SiHTML introduces a straightforward mechanism for declaring variables within HTML markup, enhancing the language's flexibility and expressiveness. Variables in SiHTML follow a simple syntax and can be used to insert values into the generated HTML output dynamically. 

- **Optional, Automatic Code Formatting with BeautifulSoup:** SiHTML offers an optional integration with BeautifulSoup4 to automatically format the generated HTML code. This feature ensures that the output HTML is clean, well-indented, and adheres to best practices, enhancing readability and maintainability. By enabling the `--formatter` option during compilation, developers can leverage BeautifulSoup4 to format their HTML effortlessly.

**Example Usage:**

Below is an example of SiHTML code compared to traditional HTML:

Traditional HTML:
```html
<!DOCTYPE HTML>
<html>
	<head>
		<title>TITLE GOES HERE</title>
		<link rel="stylesheet" href="stylesheet.css" />
	</head>
	
	<body>
		<h1 id="idName" class="className">Hello World!</h1>
		<h1 style="color:#f00;">Greetings!</h1>
		<h2>HTML does not support variables.</h2>
	</body>
</html>
```

SiHTML syntax:
```html
html
	head
		title | TITLE GOES HERE
		stylesheet | stylesheet.css

	    @var | variable_name = "SiHTML supports variables!"

		h1 #idName .className | Hello World!
		h1 | Greetings ~% style="color:#f00;"
		h2 | $variable_name
```



-----------------------------------
# Project setup:
1. Ensure you have Python 3.12.0+ installed on your OS.
2. Open up the Terminal.

- ## for Unix systems:
> 3. Copy & Paste ```python -m venv env && source env/bin/activate && pip install -r reqs.txt```

- ## for Windows:
> 3. Copy & Paste ```python -m venv env && env\Scripts\activate && pip install -r reqs.txt```



-----------------------------------
# How to compile SiHTML scripts:
The SiHTML compiler is a command line tool that has one command: ```'build'``` and three arguments:
1. ```--input_file``` (```-i```)  : The script you wish to be compiled to HTML. (script.txt)
2. ```--output_file``` (```-o```) : The name of the HTML file you wish to name. (index.html)
3. ```--formatter``` (```-f```)   : Enable the BeautifulSoup4 HTML formatter. (Set to false by default)

In the terminal
```python main.py build -i script.txt -o index.html -f True```

