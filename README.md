<h1>0x00. AirBnB clone - The console</h1>
<code>Group Project</code> <code>Python</code> <code>OOP</code>
<p>
<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png" alt="" loading="lazy" style="">
</p>
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


<p>
<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png" alt="" loading="lazy" style="">
</p>


