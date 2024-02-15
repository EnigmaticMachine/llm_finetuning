### Introduction to the Blog Post Series

We'll explore how to use cloud GPUs, set up your environment, fine-tune open source LLMs, basic evaluation of model performance, and deploying models as APIs. This series will give you  step-by-step instructions, and all codes and documentation are available in [my GitHub repository](https://github.com/EnigmaticMachine/llm_finetuning). Goal of this series is to give you a guide how to fine-tuning open-source LLMs in cloud.
#### Short Introduction to Cloud Computing for Machine Learning

The training of Large Language Models (LLMs) is a computationally intensive task, often requiring powerful hardware that can handle vast amounts of data and complex calculations.

Cloud computing platforms, like vast.ai, allowing users to rent GPUs and other computing resources on-demand. Whether you need a GPU for a few minutes to test a model or for several weeks to train a complex LLM, cloud platforms offer the flexibility to scale your resources.

Vast.ai stands out for its focus on providing low-cost cloud GPU rentals. The platform operates on a marketplace model, where GPU owners can offer their computing resources for rent, resulting in lower prices compared to traditional cloud providers.

### How Cloud GPU Renting Works

Renting a GPU on vast.ai is an easy process. Users can browse available GPUs based on their performance, cost, and location criteria. Once a suitable GPU is selected, it can be rented for the desired duration, with prices clearly listed by the hour.

In the coming sections, I will guide you through the setup process step by step, explaining how to rent a GPU on vast.ai, and how to prepare your infrastructure for fine-tuning and running open-source LLM models.


### **Getting Started with Vast.ai**

After creating your account on vast.ai and navigating through the platform, it's essential to set up an SSH connection for secure and efficient project management. Vast.ai provides clear documentation on this process, which you can find [here](https://vast.ai/docs/gpu-instances/ssh). Setting up SSH will allow you to securely connect to your rented GPU instance and transfer files, run commands, and interact with your environment directly from your local machine.

#### Selecting and Launching an Instance with the Right GPU for Your Needs:

1. **Go to the 'Search' tab** on the vast.ai console to start the process of finding the right GPU for your needs.
2. In the 'instance configuration' section, click on **'EDIT IMAGE & CONFIGURATION'**. For this tutorial, we're using the Docker image available at [pytorch/pytorch on Docker Hub](https://hub.docker.com/r/pytorch/pytorch/), specifically `pytorch:latest`. Find this image and select it in the 'Edit' tab.
3. Within the edit setup, select **'Run interactive shell server, SSH'** for Launch Mode, and enable **'Use direct SSH connection'** to ensure a smooth and direct SSH experience.
4. Click on **'Select and Save'** to confirm your image and configuration choices.
5. Change **'Disk Space To Allocate'** to 60 GB or more, depending on the size of the dataset and the requirements of your project.
6. Under **GPU Resources**, set up the GPU Total RAM to at least 12 GB to ensure your model trains efficiently without running out of memory.
7. On the right side of the screen, you'll see GPUs available for rent, along with their hourly prices. **Select and rent one** that fits your project's budget and computational needs.
8. After renting, navigate to the **'INSTANCES'** tab. Here, you'll find your instance listed. Wait until the instance status shows it's ready. Then, click on the **'Connect'** tab to receive your SSH command for connection.
9. **Using VS Code** to connect to your instance provides a seamless development experience. Here's how to set it up:
    - In VS Code, find the **'Open a Remote Window'** tab in the bottom left corner and click on it.
    - Select **'Connect to Host...'**, then **'Add New SSH Host...'**.
    - Paste the SSH command provided by vast.ai.
    - When prompted to select a configuration file for the new connection, choose **'.ssh/config'**. The default locations based on your operating system are:
        - **Mac/Linux**: `~/.ssh/config`
        - **Windows**: `C:\Users\YourUserName\.ssh\config`
    - A window will prompt you to open this config file. Here, add an **IdentityFile** directive, which is the path to your private SSH key corresponding to the public key used in your vast.ai account. For example, if your public key file is `~/.ssh/id_rsa.pub`, your IdentityFile entry in the config should point to its private counterpart, `IdentityFile ~/.ssh/id_rsa`.
    - After saving your config, return to the **'Open a Remote Window'** option in VS Code and select **'Connect to Host...'** again. Your newly added vast.ai host will be listed there.
    - Click on your vast.ai host to start the connection. A new VS Code window will open, connecting you to your remote instance. Wait for the connection to establish.

By following these detailed steps, you'll have successfully set up a powerful, cloud-based GPU environment on vast.ai.


### Conclusion and Introduction to second part of series

By now, you should have basic understanding of cloud computing platform vast.ai, how to rent GPUs, and the initial steps to set up your machine and connect to it with SSH.

In next part, "Setting Up Your Environment," we will look deeper into the technicalities of Linux, Docker, and setting up a Python environment for fine-tuning of open sourced LLMs. I'll explain the Docker image selection, explain why I choose `pytorch:latest`, and guide you through installing necessary libraries. After next part you should have a robust working environment ready for fine-tuning of open sourced LLMs.
