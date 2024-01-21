# FULL-STACK

Project Description: This project is a Full Stack web application developed using HTML, CSS, JavaScript, and jQuery on the Front End, and Python Django on the Back End.

## Image
<img src="https://i.hizliresim.com/575v6z3.png" alt="alt text" >

## Database
<img src="https://i.hizliresim.com/jwp2z0x.png" alt="alt text" >

## Usage Scenarios

### 1. Visitor Scenario

- **General Site Access:**
  - Access the system through the general site address.

- **Viewing Posts:**
  - View posts on the homepage.
  - Access details of any post.
  - View comments on posts.

- **User Registration:**
  - Access the registration processes from the login page.

### 2. User Scenario

- **Visitor Operations:**
  - Perform operations from the visitor scenario.

- **User Login:**
  - Log in as a registered user.

- **Updating Profile Information:**
  - Update profile information such as profile picture, password, phone, address, etc.

- **Post Operations:**
  - Create a new post.
  - Update and delete created posts.

- **Commenting:**
  - Comment on posts.
  - Delete own comments.

### 3. Administrator Scenario

- **User Operations:**
  - Perform operations from the user scenario.

- **Access to Admin Panel:**
  - Access the Administrator-Admin panel.

- **User and Membership Operations:**
  - Manage user addition, update, and deletion.

- **Post Operations:**
  - Manage post addition, update, and deletion.

- **Comment Operations:**
  - Manage comment addition, update, and deletion.

- **Site Settings:**
  - Manage general site settings.

## How to Run

1. Clone the project to your computer:
   ```
   git clone https://github.com/ozcanakyuz/full-stack.git
   ```

2. Create and activate a virtual environment:
   ```bash
   cd full-stack
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create the database:
   ```
   python manage.py migrate
   ```

5. Start the project:
   ```
   python manage.py runserver
   ```

6. Open your browser and go to [http://localhost:8000/](http://localhost:8000/) to view the project.

These steps provide a basic guide to run your project locally. For more details and specific configurations, please refer to the project's documentation.
