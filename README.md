# Cal Hacks 11.0 Project
<h1 align="center">AIRPOOL</h1>

![image](https://github.com/user-attachments/assets/006d0a8f-3eff-440a-a0de-b52de78ab131)

## Project Flow
![flow](https://github.com/user-attachments/assets/bb6bc52e-e215-44fc-8232-6e852e79f0bc)



## About Us
Airpool is open-source decentralized network that allows individuals and startups to contribute their unused GPU resources. By pooling these resources, we create a shared infrastructure for distributing computational services that are accessible to small companies and developers. 
This empowers them to tackle sophisticated AI models and perform large-scale data analysis without heavy upfront investment in GPU hardware.

## Tech Stack
- **Frontend**: Next.js + Typescript
- **Backend**: Python, Flask
- **Other Technologies**: Fetch.ai

## Getting Started

Follow the instructions below to set up the project on your local machine.

### Prerequisites
Make sure you have the following installed:
- Node.js
- Python 3.x
- npm (Node Package Manager)
- Poetry

### Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Raghxv11/CalHacks.git
   cd CalHacks
   ```

2. **Set up the backend:**
   ```bash
   cd server/Multi_agent
   ```

3. **Initialize and activate virtual environment:**
   We use Poetry to manage our Python environment (optional but recommended):
   ```bash
   poetry init -n && poetry shell
   ```

4. **Install uAgents Framework and other dependencies:**
   ```bash
   poetry add uagents
   ```

5. **Verify installation:**
   ```bash
   poetry show uagents
   ```

6. **Install frontend dependencies:**
   ```bash
   cd ../../client
   npm install
   ```

## Running the Project

1. **Start the Backend Server:**
   In the `server` directory:
   ```bash
   python server.py
   ```

2. **Run the Multi-Agent System:**
   In a new terminal, navigate to `server/Multi_agent` and run:
   ```bash
   python run_simulation.py
   ```

3. **Start the Frontend Development Server:**
   In another terminal, navigate to the `client` directory and run:
   ```bash
   npm run dev
   ```

4. **Access the Project:**
   Open your web browser and navigate to `http://localhost:3000`.

## Project Structure

- `/server`: Contains the backend server and multi-agent system
  - `/Multi_agent`: Houses the AirPool multi-agent system
- `/client`: Contains the frontend React application


