import requests
import json

#url = "https://o3sky-sora2api.hf.space/v1/chat/completions"
url = "https://rendersora2api.duckcloud.fun/v1/chat/completions"

payload = json.dumps({
   "model": "sora2-portrait-15s",
   "messages": [
      {
         "role": "user",
         "content": """镜头跟随一辆白色复古SUV，它装有黑色车顶行李架，沿着一条陡峭的土路飞驰而上，两旁是陡峭山坡上的松树，轮胎扬起尘土。阳光洒在SUV上，为场景投射出温暖的光芒。土路缓缓蜿蜒向远处，看不到其他车辆。道路两侧的树木是红木，间或点缀着绿色植被。从后方可以看到汽车从容地跟随道路的弯曲，仿佛正在崎岖地驾车穿越险峻的地形。土路本身被陡峭的山坡和群山环绕，蓝天清澈，飘着几丝薄云。"""
      }
   ],
   "stream": True
})
headers = {
   'Authorization': 'Bearer sk_xxx',
   'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
###
##data: {"id": "chatcmpl-1767105219616", "object": "chat.completion.chunk", "created": 1767105219, "model": "sora", "choices": [{"index": 0, "delta": 
# {"content": "```html\n<video src='https://oscdn2.dyysy.com/MP4/s_6953e2c377bc819185440082d9683a45.mp4' controls></video>\n```",
#  "reasoning_content": null, "tool_calls": null}, "finish_reason": "STOP", "native_finish_reason": "STOP"}], 
# "usage": {"prompt_tokens": 0, "completion_tokens": 1, "total_tokens": 
#1}}
###
##{
#  "task_id": "task_01ke4nbqavf1c8rwdh95sqepca",
#  "status": "success",
#  "prompt": "Style: Ultra-realistic product photography with cinematic lighting. Visual texture features glossy red ceramic body with metallic chrome accents, brushed steel bolts, and detailed engine components. Lighting quality is dramatic three-point lighting with a key light from the front-left, fill light from the back-right, and rim light accentuating edges. Color palette dominated by vibrant crimson red (#B22222), cool metallic silver (#C0C0C0), and warm espresso brown (#5C4033). Atmosphere is playful, energetic, and slightly nostalgic, evoking automotive enthusiasm.\n\nCinematography: Camera starts with a handheld medium close-up on the man pouring coffee, then transitions to a static low-angle shot as steam rises. Lens is 50mm f/2.8 shallow depth of field focusing sharply on the cup while blurring background elements. Lighting includes strong directional key light casting sharp shadows and subtle rim lighting creating volume. Mood is dynamic and engaging with a rhythmic pace matching the pouring action.\n\nScene Breakdown:\n0:00s - 0:03s: A bearded man in a black Carhartt shirt pours steaming dark coffee from a glass kettle into a red V8 engine-shaped mug resting on a rustic wooden table. Steam billows dramatically upwards. The camera tracks slightly forward as he pours.\n0:03s - 0:06s: The man lifts his head, eyes wide with delight, as steam continues to rise from the mug. He holds the kettle steady. Background shows a blurred coffee shop interior with warm ambient lighting.\n0:06s - 0:10s: Cut to a gym setting. The same mug sits on a black leather weight bench. A hand pours coffee into it from a stainless steel kettle. Steam erupts powerfully against the gym’s fluorescent lighting.\n0:10s - 0:13s: Close-up of the mug alone on the bench. Steam dissipates slowly, revealing the intricate details of its chrome valve covers and gear-like wheels. Background gym equipment is softly out of focus.\n0:13s - 0:17s: Studio shot. The mug is centered on a dark wood surface with bokeh lights in the background. The camera slowly rotates around the mug, highlighting its glossy finish and metallic textures under studio lighting.\n0:17s - 0:20s: A hand gently picks up the mug, tilting it slightly to show its design. The camera follows the motion smoothly, capturing reflections on the metal parts. The scene ends with a final close-up of the mug being held.",
#  "model": "sora2-portrait-15s",
#  "result_urls": [
#    "https://videos.openai.com/az/files/00000000-ede8-7283-a968-3642ceda0496%2Fraw?se=2026-01-07T00%3A00%3A00Z&sp=r&sv=2024-08-04&sr=b&skoid=3d249c53-07fa-4ba4-9b65-0bf8eb4ea46a&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2026-01-04T01%3A09%3A32Z&ske=2026-01-11T01%3A14%3A32Z&sks=b&skv=2024-08-04&sig=%2BLEMrOqh8rvRq22RpsyKf4T638GS6IvAyN1lNN086Sc%3D&ac=oaisdsorprwestus2"
#  ]
#}
###