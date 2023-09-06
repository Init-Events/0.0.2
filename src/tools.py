import html
from diffusers import StableDiffusionPipeline

def splitIntoArray(frame_sentences):
    return frame_sentences.split("+")

def getEmotions(user_sentence):
	#Code to get emotions here
	emotion = "happy"
	return emotion

def generateFrames(emotion, user_sentence):
	promptNum = 0

	#Insert stable diffusion here
	base = StableDiffusionPipeline.from_single_file('./data/mdjrny-v4.safetensors', use_safetensors=True) 
	#Build the prompt
	base_prompt = "masterpiece, best quality, 8k, detailed, dramatic, "
	user_prompt = base_prompt + user_sentence + " "
	full_prompt = user_prompt + emotion +" style"

	#Loop through the frames and generate images
	avatarName = "prompt_" + full_prompt + ".png"

	#Use a negative prompt to mtry to make picture better
	neg_prompt = "low res, ugly, bad hands, too many digits, bad teeth, blurry, blurred background"
	
	#V1 - Use cpu
	base.to("cuda")

	#Create the image
	image = base(prompt=full_prompt, negative_prompt=neg_prompt).images[0]
	
	#Save each image into images folder with name prompt#.png
	image.save(f"static/images/{avatarName}")
    
	#Return an array with the name of each file
	return avatarName