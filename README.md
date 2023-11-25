# ChatGPT Run Code Plugin Quickstart

Welcome to the ChatGPT Run Code plugin quickstart guide. This guide will assist you in setting up a ChatGPT plugin that allows code execution within a chat interface, using Python and ngrok for secure tunneling. Ensure you have plugin developer access before proceeding.

## Setup Locally

### Prerequisites

- Python installed on your local machine.
- Access to ChatGPT plugin development.
- ngrok installed for creating a secure tunnel to your local server due to [this bug](https://community.openai.com/t/local-plugin-failure-via-localhost-plugin-id-not-found/475197/25?u=smartmanoj).
### Installation and Setup

1. **Install Required Packages:**
   Install the necessary Python packages for this plugin:
pip install -r requirements.txt

markdown
Copy code

2. **Run the Plugin:**
Start the plugin by running:
python main.py

bash
Copy code
This command initiates the local server for the plugin.

3. **Set Up ngrok:**
To expose your local server, use ngrok:
ngrok http 5003


Replace `5003` with the port number your local server is using. ngrok will provide a URL (e.g., `https://your-ngrok-url.ngrok.io`).

### Connecting to ChatGPT

After setting up the local server and ngrok:

1. Go to [ChatGPT](https://chat.openai.com).
2. Select "Plugins" from the Model drop-down menu.
3. Click on "Plugin store" and then "Develop your own plugin".
4. Enter the ngrok URL provided (e.g., `https://your-ngrok-url.ngrok.io`) and click "Find manifest file".

Your plugin should now be installed and active. Test it by executing commands that trigger the Run Code functionality.

## Setup Remotely

For remote setup, consider platforms like Cloudflare Workers, Code Sandbox, or Replit. Follow the platform-specific guidelines for deployment.

## Getting Help

Join our [Developer Community Forum](#) for support and to connect with other plugin developers. Whether you're facing technical challenges or seeking advice, the community is here to help.
