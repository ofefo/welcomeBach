# Welcome Bach

Get a recording of a random work by Bach on every startup.

## Instalation

1. Clone the repository:

`git clone https://github.com/ofefo/WelcomeBach.git`

2. While in the repository folder, run:

`pip install -r requirements.txt`

3. Modify *mystartupscript.conf*, inserting the path to bach.py:

*At line 4:*
`exec ~/path/to/bach.py`

4. Then copy it to **/etc/init/** to be able to run the program in startup:

`sudo cp mystartupscript.conf /etc/init/`