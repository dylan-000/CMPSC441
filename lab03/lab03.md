# Prompt Engineering Process

# Step 1
#### Intention
>What is the improvement that you intend to make?
* What I intend for this first initial step is to get the model running.
* In later iterations, I would like to refine the humor aspect of the model

#### Action/Change
>Why do you think this action/change will improve the agent?
* I think that tweaking the temperature and system prompt will improve this area, because I think that having a more
creative message will be tied to the "randomness" associated with the temperature value

#### Result
>What was the result?
* The result was as expected, with a little bit of humor sprinkled throughout the story-line, however, i noticed that the model stopped reprompting with options.

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?
* I think that I need to clarify that the model must continue to prompt the user in a specific way after each response.

---

# Step 2
#### Intention
>What is the improvement that you intend to make?
* I intend to improve the formatting and output of the model so that it continues to prompt the user until they exit the loop.
* I will alter the system prompt to accomplish this.

#### Action/Change
>Why do you think this action/change will improve the agent?
* I think that specifying to the model that it must reprompt the user will provide more consistency with the responses.

#### Result
>What was the result?
* For the most part, the model was prompting the user for their inputs after each scene.
* However, there was a point where the model stopped giving the choices in the form of A, B, C, D, which is not ideal.

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?
* I need to clarify the format of the choice prompting to follow the structure that i have in mind: A, B, C, D.

---

# Step 3
#### Intention
>What is the improvement that you intend to make?
* I will improve the formatting by making it explicitly clear to the model how I want the output to be.
* I intend to have it output in an A, B, C, D manner

#### Action/Change
>Why do you think this action/change will improve the agent?
* I think that by telling it that I always want a certain format, It will adhere to that.

#### Result
>What was the result?
* My idea worked well, and after a few scnarios and encounters, the model didn't deviate from the provided format once.

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?
* I think that by telling the model that I wanted a certain output format EVERY time, it adhered to that and did not deviate.

---

# Step 4
#### Intention
>What is the improvement that you intend to make?
* The model seems to be more story focused and there doesnt seem to be much combat, so i will try to push it towards that direction with altering the system prompt.
* Also, I want to change the temperature to see if the outputs are any better.

#### Action/Change
>Why do you think this action/change will improve the agent?
* I think that by nudging the model towards action in the system prompt will effectively push it towards combat being a main mechanic.

#### Result
>What was the result?
* The model did not seem to want to move in the direction of action.
* The alteration to the system prompt also caused the model to stop formatting the choices correctly

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?
* My system prompt was poorly worded and was not specific in how I wanted the model to behave. 
* I turned the temperature too high, so maybe it was generating more unprobable sequences such as ones that did not adhere to the formatting guidelines that I specified for it.

---

# Step 5
#### Intention
>What is the improvement that you intend to make?
* I want to improve the max tokens to be higher to accomodate for the lengthy system prompt that I have.
* I also want to turn down the temperature and provide a better prompt to nudge the campaign in the direction of combat.
* I want to ensure there is a focus in format consistency and really drive that home.

#### Action/Change
>Why do you think this action/change will improve the agent?
* I altered the system prompt to specify that it should 'move towards combat and action'. I think that the model will create more action/combat scenarios now
* I have changed the max-tokens option so that it can accomodate for a larger input and output. I changed it from 100 to 300 tokens.
* To make the responses more stable, I've turned the temperature down to 2 from 5.

#### Result
>What was the result?
* The model was still prompting for choices, and even seemed to move in the direction of combat, but it was attempting to manage hp points and things like that, which is not what I want.
I just wanted the scenarios to have more action, but it would make sense that the models had been trainined on data that featured a dice rolling aspect, therefore causing it to attempt to replicate that.

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?
* I think that I just need to be more specific regarding the action aspect of the campaign and then it will function better.

---

# Step 6
#### Intention
>What is the improvement that you intend to make?
* I intend to alter the system prompt so that the model will not attempt to simulate dice rolling and tracking hp points.

#### Action/Change
>Why do you think this action/change will improve the agent?
* I think that being more descript, as I have seen, is the best method to getting the model to achieve a specific output.
* By providing a clear template for the models output, it should have a better idea on what to do.

#### Result
>What was the result?
* The model adhered to the formatting instructions and also seemed to include a bit more action than in the previouse iterations.

#### Reflection/Analysis of the result. 
>Why do you think it did or did not work?
* I think by altering the system prompt and specifying to it that i dont want any simulation aspect of the campaign, it actually listened and took that into account when it created the scenarios.

# NOTE: Iterations for this process can be seen in the attempts.txt file