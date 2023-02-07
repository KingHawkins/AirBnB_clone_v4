<h1>0x00. AirBnB clone - The console</h1>
<code>Group Project</code> <code>Python</code> <code>OOP</code>
<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230207%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20230207T085412Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=1f5b64edc2ee570ec895648c9e4752b6a5596c80b5006db9f5db4369e7e1bd62" alt="" loading="lazy" style=""></p>
<h2>Welcome to the AirBnB clone Project!</h2>
<h3>First step: Write a command interpreter to manage your AirBnB objects.</h3>
<p>This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…</p>
<h2>What is a command line interpreter</h2>
<p>Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>


1. Create a new object (ex: a new User or a new Place)
2. Retrieve an object from a file, a database etc…
3. Do operations on objects (count, compute stats, etc…)
4. Update attributes of an object
5. Destroy an object


<h2>More Info</h2>
<h3>Execution</h3>
Your shell should work like this in interactive mode:
<br/>


```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```


But also in non-interactive mode: (like the Shell project in C)
<br/>


```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```


Also tests should pass in non-interactive mode:


```bash
$ echo "python3 -m unittest discover tests" | bash
```


<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230207%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20230207T085412Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=84d83f16549fbb67a9bc22a2a74618ee68c6486536310d9f4737bf42788899db" alt="" loading="lazy" style=""></p>


