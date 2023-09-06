import html
from diffusers import StableDiffusionPipeline
import torch

def splitIntoArray(frame_sentences):
    return frame_sentences.split("+")

def getEmotions(user_sentence):
	#Code to get emotions here
	emotion = "happy"
	return emotion

def generateFrames(emotion):
	promptNum = 0

	#Insert stable diffusion here
	base = StableDiffusionPipeline.from_single_file('./data/mdjrny-v4.safetensors', use_safetensors=True) 
	#Build the prompt
	base_prompt = "masterpiece, best quality, 8k, detailed, dramatic, "
	full_prompt = base_prompt + emotion +" style"

	#Loop through the frames and generate images
	avatarName = "prompt_" + full_prompt + ".png"

	#Use a negative prompt to mtry to make picture better
	neg_prompt = "low res, ugly, bad hands, too many digits, bad teeth, blurry, blurred background"
	
	#V1 - Use cpu or cuda if the computer has a gpu to generate the image
	device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
	device = "cpu"
	base.to(device)

	with torch.no_grad():
		torch.cuda.empty_cache()
		#Create the image
		base.enable_model_cpu_offload()
		images = base(prompt=full_prompt, negative_prompt=neg_prompt, height=256, width=256).images
		image = images[0]
		print(len(images))
		#Save each image into images folder with name prompt#.png
		image.save(f"static/images/{avatarName}")
    
	#Return an array with the name of each file
	return avatarName