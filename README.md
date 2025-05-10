# Auction Hall Backend

## Overview

The Auction Hall Backend is a Python-based RESTful API designed to facilitate the creation, management, and participation in digital auctions. It serves as the server-side component for an auction platform, handling auction listings, bids, and user interactions.

## Features

- **Auction Management**: Create, update, and delete auction listings.
- **Bidding System**: Place and track bids on active auctions.
- **User Authentication**: Secure endpoints to manage user sessions and permissions.
- **Database Integration**: Persistent storage using SQLite for auction and user data.

## Technologies Used

- **Python**
- **Flask**
- **SQLite**
- **SQLAlchemy**
- **Flask-Login**
- **Flask-Migrate**

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Bernard-Calma/auction_hall_back_end.git
    cd auction_hall_back_end
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Initialize the database:

    ```bash
    flask db upgrade
    ```

5. Run the application:

    ```bash
    flask run
    ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## API Endpoints

### Authentication

- `POST /login` - User login  
- `POST /logout` - User logout  
- `POST /register` - Register a new user  

### Auctions

- `GET /auctions` - List all auctions  
- `POST /auctions` - Create a new auction  
- `GET /auctions/<id>` - View auction details  
- `PUT /auctions/<id>` - Update an auction  
- `DELETE /auctions/<id>` - Delete an auction  

### Bids

- `POST /auctions/<id>/bids` - Place a bid on an auction  

## Database Schema

The application uses SQLite with SQLAlchemy ORM. Key models include:

- `User`
- `Auction`
- `Bid`

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.
