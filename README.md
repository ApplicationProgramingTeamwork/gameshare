# Game Share
A group of friends has a lot of board games they are lending to each other and to other people. However, they have difficulties in remembering who has borrowed them. That’s why they need an application that makes it possible to keep a registry of the board games, board gamers, and the current game loans.

The application should indeed be a website that would also be open to other board gamers to sign up and start lending board games. The gamers must be able to add, edit, and delete their own board games, see all the games added to the site, borrow currently free games, return games they have borrowed, and check who has borrowed a certain game, etc.

Please note that the application doesn’t allow a gamer to have more than three borrowed games simultaneously. The application should save enough information about the different entities so that it is easy to answer questions like “What kinds of high-level characteristics does the board game have?” and “Who borrowed the game and when?”.

Any gamer trying to borrow a fourth game simultaneously should be clearly informed that they must return at least one of the old games before the system allows them to borrow a new one. The application must also keep a record of data creation dates and times, as well as the dates and times of the last modifications.

## Getting Started
It is recommended to use a virtual environment to manage your dependencies. You can create and activate a virtual environment by running the following commands:
```shell
python -m .venv .venv
```

Activate the virtual environment on Macos/Linux
```shell
source .venv/bin/activate  
```

On Windows
```shell
.venv\Scripts\activate
```

Once the virtual environment is activated, you can install the required dependencies:
```shell
pip install -r requirements.txt
```

Then, create a `.env` file in the root directory with the following content
```shell
DATABASE_URL="postgresql://username:password@localhost:5432/gameshare"
```

## UML
```mermaid
classDiagram
  class Gamer {
    CharField username
    DateTimeField joined_date
    ForeignKey owner
    str __str__()
    bool can_borrow()
  }

  class BoardGame {
    CharField name
    ForeignKey owner
    CharField genre
    TextField description
    DateTimeField created_at
    DateTimeField updated_at
    ImageField image
    str __str__()
  }

  class Loan {
    ForeignKey board_game
    ForeignKey gamer
    DateTimeField loaned_at
    DateTimeField return_by
    str __str__()
    bool is_overdue()
  }

  Gamer "1" --> "0..*" BoardGame : owns
  Gamer "1" --> "0..*" Loan : borrows
  BoardGame "1" --> "0..*" Loan : is borrowed by
```

## TODO

### ⁠Backend Development and Model Design
Task Leader A: Responsible for designing primary database models.
Subtasks:
Model Definitions: Create BoardGame, User, and Loan models with the necessary fields and relationships.
Data Validation and Loan Logic: Implement the 3-game loan limit using a function like can_borrow() to handle borrowing restrictions, ensuring it’s easy for others to access.
Database Migration and Initial Testing: Perform migrations and initial tests to verify the models are working as intended.
Collaboration Note: After development, Task Leader A should document the can_borrow() function and relevant model interfaces for other members to reference easily.

### ⁠⁠User Authentication and Account Management
Task Leader B: Handles user registration, login, logout, and access restrictions.
Subtasks:
User System: Implement registration, login, and logout functionality with access control using decorators like login_required.
Loan Limit and Error Messaging: Integrate the loan limit by calling A’s can_borrow() function and displaying error messages if the limit is exceeded.
Permissions and Security: Set permissions to ensure users can only edit their own information and add basic security features (e.g., CSRF protection).
Collaboration Note: Once authentication is complete, Task Leader B should coordinate with A to document main access logic post-login to maintain consistent permissions.

### ⁠Frontend Development and Template Design
Task Leader C: Designs site pages and overall appearance, ensuring consistent styling using template inheritance.
Subtasks:
Base Template: Create a base.html template with common elements (header, navbar, footer).
Page Designs: Build pages for the board game list, game details, user loan history, and loan/return buttons.
Loan Prompt and Restrictions: Dynamically display loan status on the page (using the can_borrow() result from templates) and show an alert if the loan limit is exceeded.
Collaboration Note: Task Leader C should clarify data needs and endpoints from A and B in advance to ensure front-end display accuracy and set placeholders for easy data integration later.

### Project Management, Code Integration, and Documentation
Task Leader D: Manages Git, code integration, documentation, and testing.
Subtasks:
Git Management and Code Merging: Set up the Git repository, oversee code merging, resolve conflicts, and make regular backups.
Integration Testing: Conduct integration tests across modules to ensure seamless data flow between pages and correct user access.
Documentation: Prepare documentation for interfaces, functionality, and code comments, and draft the team report outlining task allocation and contributions.
Collaboration Note: Task Leader D should communicate regularly with all members to identify any issues with integration and update documentation based on module feedback.


## Instruction
The group work commission is to create a Django based web site by using Python programming language. 

A permanent data storage must be used. (For a special request other technologies might be accepted)
The group size is almost without exception 5 students. The groups are formed according to your own instructor’s principles.

The group has 2 alternatives: To make the web site on the subject given by the instructors or to make the web site on the group members’ own subject. 

The groups’ own subject of the web site must be accepted by the instructor before the group can start working on it. Before suggesting anything read through the evaluation criteria given later in this document. Another alternative is to implement a web site shortly described below. 

The instructors’ subject is described below:
> "A group of friends has a lot of board games they are lending to each other and to other people. However, they have difficulties in remembering who has borrowed them. That’s why they need an application making it possible to keep a registry of the board games, board gamers, and the current game loans. The application should indeed be a web site that would also be open to other board gamers to sign up and start lending board games. The gamers must be able to add, edit and delete their own board games, to see all the games added to the site, to borrow currently free games, to return games they have borrowed, check who has borrowed a certain game, etc. Please note that the application doesn't allow a gamer to have more than 3 borrowed games simultaneously. The application should save enough information about the different entities so that it is easy to answer the questions like “What kinds of high-level characteristics the board game has?” and “Who borrowed the game and when?”. Any gamer trying to borrow the 4th game simultaneously should be clearly informed that he must return at least one of the old games before the system allows him to borrow a new one. The application must also keep record of data creation dates and times, as well as the dates and times of last modifications."

In case you decide to implement a web site for the group members’ own subject, please post a short description of your group’s suggested subject into itsLearning announcement “Teamwork Subjects for Acceptance” no later than November 1 2024 midnight. It is enough that one member of the group returns the description but take care that the group is mentioned in the posting. The instructor will then comment and accept/reject it. In case you decide to implement the board game web game site explained above, one member of your group should just post the group number and a message “Board Game Web Site”. No instructor’s acceptance is required in that case.

The evaluation will happen by demonstrating 1) the functioning web site and 2) the source code to the instructor and other students online. Please, write a short note “For Teamwork Evaluation” (about one or two pages long) where you describe the idea of your web site and suggest a grade you deserve. In that note, pay special attention for the reasons behind your grade suggestion. Also, it is very important that the document clarifies who has done what, especially if Git is not used. Return this note to the itsLearning no later than at least 2 days before your group’s agreed presentation session.

The presentation sessions will be arranged during reservable times on week starting at Mon 18 November. You can also suggest and agree an earlier time for presentation directly with your instructor. 
The maximum number of points available from the teamwork is 20.

Please note that the personal points of team members can vary. A passive member can be left totally without points. An especially active and cooperative member pointed out by the other members can get some extra points. All the members must participate in programming actively.

The evaluation criteria implemented is below. The text inside [] brackets is a reference to the subject given above.

The minimum requirement for an accepted teamwork is 8 points. 

To earn that it is expected that
-	the web site is implemented for an accepted subject, (required)
-	the implemented web site functions, (2 points)
-	MVT architecture is obeyed, (2 points)
-	there must be more than 1 model, (2 points)
-	users [board gamers] can view a list of all [available board games] entities of one kind, (1 points)
-	a user [a board gamer] can add an entity [a board game], (1 points)
-	a user can do something for an entity [a board gamer can borrow a board game]. (1 points)
-	the web site and its source code are presented online to the instructor in agreed time (required)

More points can be earned by fulfilling the following requests:
-	a user [a board gamer] can edit instances to at least 2 models [(not only a board game)], (1 points)
-	template inheritance is used, (1 point)
-	user accounts have been set up (1 point)
-	no gamer can borrow than 3 games simultaneously (1 point)
-	a gamer is clearly informed the reason he can’t borrow the 4h game simultaneously  (1 point)
-	login and logout functionality has been implemented (1 points)
-	sign-up functionality has been implemented, (1 points)
-	restricted access has been implemented, (1 points)
-	information security is considered, at least partly, (1 points)
-	Django admin site is functioning for the application and the superuser is created, (1 point)
-	the web site looks good and is styled (1 points)

You can earn extra 2 points by managing the project’s source code and collaborative development in a Git repository.

In case you not receiving full 20 points, you can try to get 1 to 2 points by using some libraries or implementing some functionalities that were not included in the book and lectures.