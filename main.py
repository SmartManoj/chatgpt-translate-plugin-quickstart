import json
import quart
import quart_cors
from quart import request
from api import talk
app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")


@app.route('/talk', methods=['POST'])
async def talk_route():
    data = await request.get_json(force=True)
    text_to_talk = data.get('text')
    response = talk(text_to_talk)
    return json.dumps({'response': response})


@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)