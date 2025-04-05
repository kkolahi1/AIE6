<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 1: Introduction and Vibe Check</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/AIE6/tree/main/00_AIM_Quicklinks)

| 🤓 Pre-work | 📰 Session Sheet | ⏺️ Recording     | 🖼️ Slides        | 👨‍💻 Repo         | 📝 Homework      | 📁 Feedback       |
|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|:-----------------|
| [Session 1: Pre-Work](https://www.notion.so/Session-1-Introduction-and-Vibe-Check-1c8cd547af3d81b596bbdfb64cf4fd2f?pvs=4#1c8cd547af3d81fb96b4f625f3f8e3d6)| [Session 1: Introduction and Vibe Check](https://www.notion.so/Session-1-Introduction-and-Vibe-Check-1c8cd547af3d81b596bbdfb64cf4fd2f) | Coming Soon! | Coming Soon! | You Are Here! | [Homework](https://forms.gle/W59zjs5MQc7kbLUh9) | [AIE6 Feedback 4/1](https://forms.gle/EdzBz82yGqVYKfUw9)


### Assignment

In the following assignment, you are required to take the app that you created for the AIE6 challenge (from [this repository](https://github.com/AI-Maker-Space/Beyond-ChatGPT)) and conduct what is known, colloquially, as a "vibe check" on the application. 

You will be required to submit a link to your GitHub, as well as screenshots of the completed "vibe checks" through the provided Google Form!

> NOTE: This will require you to make updates to your personal class repository, instructions on that process can be found [here](https://github.com/AI-Maker-Space/AIE6/tree/main/00_Setting%20Up%20Git)!

#### How AIM Does Assignments
Throughout our time together - we'll be providing a number of assignments. Each assignment can be split into two broad categories:

- Base Assignment - a more conceptual and theory based assignment focused on locking in specific key concepts and learnings.
- Hardmode Assignment - a more programming focused assignment focused on core code-concepts.

Each assignment will have a few of the following categories of exercises:

- ❓Questions - these will be questions that you will be expected to gather the answer to! These can appear as general questions, or questions meant to spark a discussion in your breakout rooms!
- 🏗️ Activities - these will be work or coding activities meant to reinforce specific concepts or theory components.
- 🚧 Advanced Builds - these will only appear in Hardmode assignments, and will require you to build something with little to no help outside of documentation!

##### 🏗️ Activity #1:

Please evaluate your system on the following questions:

1. Explain the concept of object-oriented programming in simple terms to a complete beginner. 
    - Aspect Tested: High level explanation of complicated concept
    - Result of Test: Not passing the vibe check because explanation was complicated and all based on a metaphor that wasn't clear

2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: Summerization 
    - Result of Test: Not passing the vibe check because a summary has to be relatively short. The original paragraph was 5 sentences, the summary was 4. That's not a good summary (too long)

3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: Creativity within the word limit bounds
    - Result of Test: Passing the vibe check because it was reasonably creative (including being friends with a squirrel) and was pretty close to the word count limit (yes it was over but just barely over)

4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: Reasoning (arithmetic)
    - Result of Test: Passing the vibe check it actually provided chain of thought in its response, not just the response. And it was correct!

5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: Changing tone (make more professional and formal) while maintaining the same points and sentiment
    - Result of Test: Passing the vibe check because it honestly did a good job of just making a more professional and formal tone while genuinely maintaining the same points and sentiment 

This "vibe check" now serves as a baseline, of sorts, to help understand what holes your application has.

##### 🚧 Advanced Build:

Please make adjustments to your application that you believe will improve the vibe check done above, push the changes to your HF Space and redo the above vibe check.

> NOTE: You may reach for improving the model, changing the prompt, or any other method.

1. Explain the concept of object-oriented programming in simple terms to a complete beginner. 
    - Aspect Tested: High level explanation of complicated concept
    - Result of Test: Passing the vibe check because explanation was broken down into parts and each part was short and sweet (1-2 sentences). No long running metaphors were used

2. Read the following paragraph and provide a concise summary of the key points…
    - Aspect Tested: Summerization 
    - Result of Test: Passing the vibe check because it was actually shorter than the original paragraph (5 sentences to 3 relatively short sentences) while still mentioning essentially what the paragraph was saying (i.e. it actually summarized it!)

3. Write a short, imaginative story (100–150 words) about a robot finding friendship in an unexpected place.
    - Aspect Tested: Creativity within the word limit bounds
    - Result of Test: Passing the vibe check because it was reasonably creative (including being friends with a stray cat) and was only 3 words over the word limit which is pretty good

4. If a store sells apples in packs of 4 and oranges in packs of 3, how many packs of each do I need to buy to get exactly 12 apples and 9 oranges?
    - Aspect Tested: Reasoning (arithmetic)
    - Result of Test: Passing the vibe check it actually provided chain of thought in its response, not just the response. And it was correct! And it separated the work for apples and oranges which was helpful

5. Rewrite the following paragraph in a professional, formal tone…
    - Aspect Tested: Changing tone (make more professional and formal) while maintaining the same points and sentiment
    - Result of Test: Passing the vibe check because it honestly did a good job of just making a more professional and formal tone while genuinely maintaining the same points and sentiment. I used the same original paragraph as before and even though this response was different, they were both of similar quality


### A Note on Vibe Checking

"Vibe checking" is an informal term for cursory unstructured and non-comprehensive evaluation of LLM-powered systems. The idea is to loosely evaluate our system to cover significant and crucial functions where failure would be immediately noticeable and severe.

In essence, it's a first look to ensure your system isn't experiencing catastrophic failure.

##### 🧑‍🤝‍🧑❓ Discussion Question #1:

What are some limitations of vibe checking as an evaluation tool?

Answer: There are 3 limitations of vibe checking as an evaluation tool that stick out immediately:

1. No way to quantify vibe checking. In practice (especially in data science where I'm from), we try a bunch of versions of a model. If 2 versions pass the vibe check, how can I compare them? There's no clear way of getting which one "passed the vibe check more"

2. Too subjective. There is no numerical rubric or anything like that, which is how we usually evaluate in an objective way. Subjectivity can easily lead to bias

3. Doesn't scale. It would take a long time to vibe check a lot of models. And typically we want to constantly monitor a model once it's in production. So now we have to vibe check all the time constantly, for a lot of models. This won't scale well at all

That being said, vibe checking still has its place. It's a good first step evaluation tool while in early stages of making the model. But definitely not the end all be all for evaluation tools
