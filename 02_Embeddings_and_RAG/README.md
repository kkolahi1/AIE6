<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">Session 2: Embeddings and RAG</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE6/tree/main/00_AIM_Quicklinks)

| 🤓 Pre-work | 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Session 2: Pre-Work](https://www.notion.so/Session-2-Embeddings-Retrieval-Augmented-Generation-RAG-1c8cd547af3d81978a5af041c0d5b30a?pvs=4#1c8cd547af3d818daab3db56a5e631e9)| [Session 2: Embeddings, Retrieval Augmented Generation (RAG)](https://www.notion.so/Session-2-Embeddings-Retrieval-Augmented-Generation-RAG-1c8cd547af3d81978a5af041c0d5b30a) | [Recording](https://us02web.zoom.us/rec/share/gSn6QuqteVM4gYK9SslqMLx4MRVcwVj1S9RT-wJQYUuSVBkJ14-Fj8qY8d7Tyx-9.7ijgK2xRDpWFZ-bu) (lz2MTcF=)| [Session 2: Embeddings and RAG](https://www.canva.com/design/DAGjaSBtoao/n8G0T_O-2OIQHvgTfqyAxg/edit?utm_content=DAGjaSBtoao&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) | You Are Here! | [Session 2 Assignment: Embeddings & RAG](https://forms.gle/FNkAuvdZe8eiaLTC8)| [AIE6 Feedback 4/3](https://forms.gle/iDTwhJ2nLp5CGkqP6)


### Outline:

🤜 BREAKOUT ROOM #1:
- Task 1: Imports and Utilities
- Task 2: Documents
- Task 3: Embeddings and Vectors
- Task 4: Prompts
- Task 5: Retrieval Augmented Generation
     - 🚧 ACTIVITY #1: Augment RAG

### Steps to Run:

1. Install UV - which you can do through [this resource](https://docs.astral.sh/uv/#getting-started)
2. Run the command `uv sync`
3. Open your Jupyter notebook and select `.venv` for your kernel. 

# Build 🏗️

Run the notebook!

# Ship 🚢

- Add one of the following "extras" to the RAG pipeline:
     - Allow it to work with PDF files
     - Implement a new distance metric
     - Add metadata support to the vector database
- Make a simple diagram of the RAG process
- Run the notebook
- Record a Loom walking through the notebook, the questions in the notebook, and your addition!

# Share 🚀
- Show your App in a loom video and explain the diagram
- Make a social media post about your final application and tag @AIMakerspace
- Share 3 lessons learned
- Share 3 lessons not learned

Here's a template to get your post started!

```
🚀 Exciting News! 🎉

I just built and shipped my very first Retrieval Augmented Generation QA Application using Chainlit and the OpenAI API! 🤖💼 

🔍 Three Key Takeaways:
1️⃣ The power of combining traditional search methods with state-of-the-art generative models is mind-blowing. 🧠✨
2️⃣ Collaboration and leveraging community resources like AI Makerspace can greatly accelerate the learning curve. 🌱📈
3️⃣ Dive deep, keep iterating, and never stop learning. Each project brings a new set of challenges and equally rewarding lessons. 🔄📚

A huge shoutout to the @AI Makerspace for their invaluable resources and guidance. 🙌

Looking forward to more AI-driven adventures! 🌟 Feel free to connect if you'd like to chat more about it! 🤝

#OpenAI #Chainlit #AIPowered #Innovation #TechJourney
```
## API Key Setup

### Local Development
1. Create a `.env` file in the project directory
2. Add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

### Deployment
- **GitHub**: Use repository secrets
- **Huggingface**: Use Space secrets
- **Other platforms**: Use their environment variable systems

> Note: Make sure to add `.env` to your `.gitignore` file to keep your API key secure.


##### ❓ Question #1:

The default embedding dimension of text-embedding-3-small is 1536.

1. Is there any way to modify this dimension?

Answer: Yes! There is an optional parameter called `dimensions`, which is an integer, which allows you to REDUCE the number of dimensions (but not increase), which is done in a smart way as described below

2. What technique does OpenAI use to achieve this?

Answer: OpenAI uses Matryoshka Representation Learning (MRL), which is a smart way to make the embeddings. The basic idea is this: the dimensions progress from course to fine granularity, so if you need to reduce the dimensions (e.g. for speed or cost reasons), you can just keep the first n dimensions (where n is the number of dimensions you want) and throw the rest of the dimensions away. Then you just to need normalize the vector (which now only has n dimensions). This just means find its L2 norm (i.e. Euclidean norm) and divide by it (unless of course it is 0)


##### ❓ Question #2:

What are the benefits of using an `async` approach to collecting our embeddings?

Answer: Let's first start with the difference between `async` and `sync`: essentially, `sync` executes operations one at a time (e.g. must finish one operation before moving on to the next). On the other hand, `async` executes multiple operations concurrently (it does NOT have to finish one operation before moving on to the next)

Well, looking at our code, we use the method `abuild_from_list`, which itself calls `async_get_embeddings`, which is `async` and this is where the time savings really comes in: instead of making a API call to our OpenAI embedding model for each chunk, `async_get_embeddings` makes just one API call per batch. Since it can handle batch size of 1024 and we only have 373 chunks, that means we only need to make one API call for all of our chunks. This is a huge time saver as API calls really slow things down (it's not like we are using a crazy amount of computing power, we are just waiting to make the API connection)


