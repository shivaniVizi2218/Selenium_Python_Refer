## Introduction 

EOS Automation Regression is a Pytest project build using Selenium Webdriver written in Python.

### Prerequisites
#### Installation process
1. Python Installed : Ensure that Python is installed on your system. We can download and install Python from the official Python website (https://www.python.org/). Ensure latest version of python(python 3.12.3) is downloaded in your system.
2. PyCharm Installed : Download and install PyCharm IDE from JetBrains website (https://www.jetbrains.com/pycharm/). PyCharm comes in two editions: Community (free) and Professional (paid). The Community edition should be fine for most Selenium automation Frameworks.
3. Git Installed : To clone the automation framework from a Git repository,Git need to be installed on your system. You can download Git from the official website (https://git-scm.com/).
4. pip installed : Download the get-pip.py script from the official Python website
      ```
      run the following commad in command prompt or in terminal:
             curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
      Then, run the following command to install pip:
             python get-pip.py
      Verify pip is installed by following command.
             pip --version
     ```

### Cloning Repo
1. Open Terminal or Command Prompt : Open the terminal (macOS/Linux) or command prompt(Windows) on your computer.
2. Navigate to the Directory Where You Want to Clone the Repository : Use the cd command to navigate to the directory where you want to clone the repository. You can use: 
````
   cd ./desired directory
````                              
3. Clone the Repository : Once you're in the desired directory, use the git clone command followed by the URL of the repository you want to clone.
        For example : 
```
   git clone https://github.com//git_url.
```

4. Authenticate (if required) : If the repository is private and requires authentication, Git will prompt you to enter your username and password.
5. Wait for the Clone to Complete : Git will start cloning the repository to your local machine. Depending on the size of the repository and your internet connection speed, this process may take some time. Once the clone is complete, you'll see a message indicating that the clone was successful.
6. Navigate to the Cloned Repository : After the clone is complete, you can navigate into the cloned repository's directory using the cd command.
        For example 
```
    cd repository name
```
### Create a virtual environment in Python in Project Directory :- 
1. Open Terminal or Command Prompt : Open the terminal(macOS/Linux) or command prompt(Windows) on your computer.
2. Navigate to the Directory Where You Want to Create the Virtual Environment : Use the cd command to navigate to the directory where you want to  create the virtual environment. For example, if you want to create it in your project directory, 
        navigate to that directory using:
```
    cd path/to/your/project/directory
```
3. Create the Virtual Environment : Once you're in the desired directory, use the following command to create a virtual environment named "venv":
```        
   python -m venv .venv
```
4. Activate the Virtual Environment : After creating the virtual environment, you need to activate it. The activation process varies depending on your  
   Operating system: Mac OS :- 
````    
         source .venv/bin/activate
````
   Windows (Command Prompt) :- 
````       
         .venv/Scripts/activate
````
5. Deactivate the Virtual Environment (Optional) : To deactivate the virtual environment and return to your global Python environment, simply use the deactivate command: deactivate

### Install of all necessary Libraries and packages :- 
    
1. Open Terminal or Command Prompt : open command prompt or terminal and navigate to project directory.

2. Activate Virtual Environment : Activate Virtual environment in automation project directory.

3. Install All dependencies : Install all dependencies using pip install command
    ````     
   pip install selenium
   pip install pytest 
   pip install webdriver-manager
   pip install pandas
   pip install openpyxl
   ````
### Run Test cases  :- 
Open the command prompt and run pytest to run specific test cases.
```
    pytest path/to/your/test_file.py
```

