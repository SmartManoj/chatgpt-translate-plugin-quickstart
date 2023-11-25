import json
import quart
import quart_cors
from quart import request
from api import run_code
app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")


@app.route('/run_code', methods=['POST'])
async def translate_route():
    data = await request.get_json(force=True)
    code = data.get('code')
    out,err = (run_code(code))
    return json.dumps({'stdout':out, 'stderr':err})


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