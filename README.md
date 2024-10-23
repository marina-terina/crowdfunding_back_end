# Crowdfunding Back End
KICKAROO

## Planning:
### Concept/Name
Kickaroo is a crowdfunding platform designed to help people bring their wildest, most unconventional ideas to life. The platform appeals to innovators, artists, and adventurers who are ready to kickstart something crazy and unique. Whether it's a quirky invention, an offbeat project, or a bold business concept, Kickaroo provides a fun, community-driven space for creative minds to share their ideas and fundraise for them. Backers get to support out-of-the-box projects while being an integral part of exciting and unconventional journeys. They will have the chance, for example, to receive exclusive offers, behind-the-scenes access, the opportunity to follow the journey, or early bird perks that allow them to enjoy rewards and products before they are available to the general public.

### Intended Audience/User Stories
Intended Audience
- Creative Entrepreneurs: People with unconventional ideas, looking for a fun and engaging way to fund their projects.
- Artists & Designers: Creatives wanting to showcase offbeat, innovative works, and fund their artistic projects.
- Adventure Seekers & Experience Creators: Individuals with unique travel or experiential ideas, looking for support from like-minded backers.
- Startups & Small Businesses: Small businesses with bold, niche products or services that need funding to get off the ground.
- Community Groups & Local Innovators: Groups or individuals creating quirky, community-focused initiatives who need crowd support.
- Backers Seeking Unique Projects: Supporters interested in exploring and backing wild, one-of-a-kind ideas.

User Stories

       As a Creator:
- "I want to share my unconventional project and raise funds to bring my bold idea to life".
- "I want to set funding goals and deadlines for my project to keep backers informed and engaged".
- "I want to offer backers the opportunity to be engaged participants in my project, for example, by providing access to a closed channel where they can see exclusive updates, behind-the-scenes content, and early prototypes, so they feel connected to the journey."
- "I want to provide early bird perks to my backers, allowing them to enjoy rewards and products before they are available to the general public."

      As a Backer:
- "I want to easily browse and discover creative projects so that I can find ideas that excite me."
- "I want to see clear descriptions and funding goals so I can choose the best projects to back."
- "I want to make an anonymous pledge, so I can support the creator while maintaining my privacy."
- "I want to add a comment to accompany the pledge."
- "I want to receive exclusive updates and insights about the projects I support so that I can feel involved and informed throughout the process."

### Front End Pages/Functionality 
         1. Home Page functionality:
- Navbar and Login Button: For easy navigation to key sections and access to user accounts.
- Overview of Featured Projects: This section is designed to encourages users to explore projects, engage with projects, and back projects. 
  Each featured project will include: Title, Owner (a user), Description, Image, Target amount, status, timestamp, perks and Button "Kick Me Mate!" 
- Call-to-Action Buttons for Creators: Prominent buttons "Kickstart Your Idea" inviting creators to start their projects.

         2. Login/Register Page functionality:
- User registration form for new users (Fields:Username, Email address, Password).
- Login form for returning users(Fields: Email address or username, Password).

          3. Project Creation page "Kickstart Your Idea":
- This page allows users to provide all necessary details to create a project. 
  Project details includes:
       *Title
       *Owner (a user)
       *Description
       *Image 
       *Target amount to fundraise
       *Status
       *Timestamp
       *Perks

         4. Pledge Creation Page "Kick Me Mate!":
- This page allows users to make pledges easily.  
  Pledge details includes:
        *Amount pledged
        *Option to make the pledge anonymous or not
        *A comment to accompany the pledge
        *Desire to receive a perks (if anonymous - no perks).

        5. User Dashboard: A page for users to view and manage their created projects and pledges.
         
          
### API Spec
| URL                 | HTTP Method | Purpose                           | Request Body                                                                                                                                  | Success Response Code | Authentication/Authorization             |
|---------------------|-------------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------------------------------|
| /users              | POST        | Register a new user               | { "first_name": "string", "last_name": "string", "username": "string", "email": "string", "password": "string" }                              | 201 Created           | None                                     |
| /api-token-auth/     | POST        | Authenticate user                 | { "username_or_email": "string", "password": "string" }                                                                                       | 200 OK                | None                                     |
| /projects            | GET         | Retrieve featured projects        | None                                                                                                                                          | 200 OK                | None                                     |
| /projects            | POST        | Create a new project              | { "title": "string", "description": "string", "goal": "Integer", "image": "url", "reward": "string", "is_open": "boolean", "owner": "user_id" }| 201 Created           | Must be logged in                        |
| /projects/id         | GET         | Retrieve project details          | None                                                                                                                                          | 200 OK                | None                                     |
| /projects/id         | PUT         | Update project details            | { "title": "string", "description": "string", "goal": "Integer", "image": "url", "reward": "string", "is_open": "boolean" }                    | 200 OK                | Must be logged in & owner                |
| /projects/id         | DELETE      | Delete a project                  | None                                                                                                                                          | 204 No Content        | Must be logged in & owner                |
| /user/id            | PUT         | Update user details               | { "first_name": "string", "last_name": "string", "username": "string", "email": "string", "password": "string" }                               | 200 OK                | Must be logged in (update own details)   |
| /user/id/projects    | GET         | Retrieve user's own projects      | None                                                                                                                                          | 200 OK                | Must be logged in & owner (retrieve own) |
| /user/id/pledges     | GET         | Retrieve user's own pledges       | None                                                                                                                                          | 200 OK                | Must be logged in (retrieve own)         |
| /pledges             | POST        | Create a pledge for a project     | { "amount": "number", "anonymous": "boolean", "comment": "string", "supporter": "user_id", "accept_reward": "boolean" }                        | 201 Created           | Must be logged in                        |
| /pledges             | GET         | Retrieve all pledges              | None                                                                                                                                          | 200 OK                | None                                     |
| /pledges/id          | PUT         | Update a pledge                   | { "amount": "number", "anonymous": "boolean", "comment": "string", "accept_reward": "boolean" }                                                | 200 OK                | Must be logged in & pledge owner         |
| /pledges/id          | DELETE      | Delete a pledge                   | None                                                                                                                                          | 204 No Content        | Must be logged in & pledge owner         |
| /users/id/           | DELETE      | Delete a user                     | None                                                                                                                                          | 204 No Content        | Must be logged in & owner                |
### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )