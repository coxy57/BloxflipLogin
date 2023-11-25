import hashlib
from Crypto.Cipher import AES
import string,random, json, time, secrets
import tls_client
from PIL import Image
import io
import base64

# made by coxy.57
# made by coxy.57
# made by coxy.57
# made by coxy.57
# made by coxy.57
# made by coxy.57
# made by coxy.57
# thanks to pr0ton for the encrypt and decrypt func :)



class BloxflipLogin:
    def __init__(self):
        self.t = tls_client.Session(client_identifier="Chrome119")
        self.coxy = "coxy.57"
        self.coxy_ = "coxy.57"
        self.coxy_ = "coxy.57"
        self.user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    def gen_cfp(self):
        try:
            b1 = Image.new('RGB', (200, 200), color='white')
            b2 = []
            buffer = io.BytesIO()
            b1.save(buffer, format='PNG')
            b2.append("canvas winding:yes")
            b2.append('fp:data:image/png;base64,' + base64.b64encode(buffer.getvalue()).decode())
            return "~".join(b2)
        except Exception as e:
            return f"error with cfp: {e}"

    def decrypt_bda(self,data):
        ts = time.time()
        timeframe = int(ts - ts % 21600)
        user_agent = self.user_agent + str(timeframe)

        data = json.loads(data)
        dk = user_agent.encode() + bytes.fromhex(data["s"])
        md5 = [hashlib.md5(dk).digest()]
        result = md5[0]
        for i in range(1, 3 + 1):
            md5.insert(i, hashlib.md5((md5[i - 1] + dk)).digest())
            result += md5[i]

        aes = AES.new(result[:32], AES.MODE_CBC, bytes.fromhex(data["iv"]))
        data = aes.decrypt(base64.b64decode(data["ct"]))
        return data.decode()

    def encrypt(self,data, key):
        data = data + chr(16 - len(data) % 16) * (16 - len(data) % 16)

        salt = b"".join(random.choice(string.ascii_lowercase).encode() for _ in range(8))
        salted, dx = b"", b""
        while len(salted) < 48:
            dx = hashlib.md5(dx + key.encode() + salt).digest()
            salted += dx

        key = salted[:32]
        iv = salted[32 : 32 + 16]
        aes = AES.new(key, AES.MODE_CBC, iv)

        encrypted_data = {
            "ct": base64.b64encode(aes.encrypt(data.encode())).decode("utf-8"),
            "iv": iv.hex(),
            "s": salt.hex(),
        }
        return json.dumps(encrypted_data, separators=(",", ":"))

    def get_bda(self) -> str:
        ts = time.time()
        timeframe = int(ts - ts % 21600)
        key = self.user_agent + str(timeframe)
        gen = self.gen_cfp()
        the_data = [
            {"key": "api_type", "value": "js"},
            {"key": "p", "value": 1},
            {"key": "f", "value": secrets.token_hex(16)},
            {"key": "n", "value": time.time()},
            {
                "key": "wh",
                "value": f"{secrets.token_hex(16)}|{secrets.token_hex(16)}",
            },
            {
                "key": "enhanced_fp",
                "value": [
                    {
                        "key": "webgl_extensions",
                        "value": "ANGLE_instanced_arrays;EXT_blend_minmax;EXT_color_buffer_half_float;EXT_disjoint_timer_query;EXT_float_blend;EXT_frag_depth;EXT_shader_texture_lod;EXT_texture_compression_bptc;EXT_texture_compression_rgtc;EXT_texture_filter_anisotropic;EXT_sRGB;KHR_parallel_shader_compile;OES_element_index_uint;OES_fbo_render_mipmap;OES_standard_derivatives;OES_texture_float;OES_texture_float_linear;OES_texture_half_float;OES_texture_half_float_linear;OES_vertex_array_object;WEBGL_color_buffer_float;WEBGL_compressed_texture_s3tc;WEBGL_compressed_texture_s3tc_srgb;WEBGL_debug_renderer_info;WEBGL_debug_shaders;WEBGL_depth_texture;WEBGL_draw_buffers;WEBGL_lose_context;WEBGL_multi_draw",
                    },
                    {
                        "key": "webgl_extensions_hash",
                        "value": secrets.token_hex(16),
                    },
                    {"key": "webgl_renderer", "value": "WebKit WebGL"},
                    {"key": "webgl_vendor", "value": "WebKit"},
                    {"key": "webgl_version", "value": "WebGL 1.0 (OpenGL ES 2.0 Chromium)"},
                    {
                        "key": "webgl_shading_language_version",
                        "value": "WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)",
                    },
                    {"key": "webgl_aliased_line_width_range", "value": "[1, 1]"},
                    {"key": "webgl_aliased_point_size_range", "value": "[1, 1024]"},
                    {"key": "webgl_antialiasing", "value": "yes"},
                    {"key": "webgl_bits", "value": "8,8,24,8,8,0"},
                    {
                        "key": "webgl_max_params",
                        "value": "16,32,16384,1024,16384,16,16384,30,16,16,4095",
                    },
                    {"key": "webgl_max_viewport_dims", "value": "[32767, 32767]"},
                    {"key": "webgl_unmasked_vendor", "value": "Google Inc. (NVIDIA)"},
                    {
                        "key": "webgl_unmasked_renderer",
                        "value": "ANGLE (NVIDIA, NVIDIA GeForce GTX 1050 Ti (0x00001C82) Direct3D11 vs_5_0 ps_5_0, D3D11)",
                    },
                    {"key": "webgl_vsf_params", "value": "23,127,127,23,127,127,23,127,127"},
                    {"key": "webgl_vsi_params", "value": "0,31,30,0,31,30,0,31,30"},
                    {"key": "webgl_fsf_params", "value": "23,127,127,23,127,127,23,127,127"},
                    {"key": "webgl_fsi_params", "value": "0,31,30,0,31,30,0,31,30"},
                    {"key": "webgl_hash_webgl", "value": secrets.token_hex(16)},
                    {
                        "key": "user_agent_data_brands",
                        "value": "Google Chrome,Chromium,Not?A_Brand",
                    },
                    {"key": "user_agent_data_mobile", "value": False},
                    {"key": "navigator_connection_downlink", "value": 6.15},
                    {"key": "navigator_connection_downlink_max", "value": None},
                    {"key": "network_info_rtt", "value": random.randint(25,50)},
                    {"key": "network_info_save_data", "value": False},
                    {"key": "network_info_rtt_type", "value": None},
                    {"key": "screen_pixel_depth", "value": 24},
                    {"key": "navigator_device_memory", "value": random.randint(8,20)},
                    {"key": "navigator_languages", "value": "en-US,en"},
                    {"key": "window_inner_width", "value": 350},
                    {"key": "window_inner_height", "value": 250},
                    {"key": "window_outer_width", "value": 350},
                    {"key": "window_outer_height", "value": 250},
                    {"key": "browser_detection_firefox", "value": False},
                    {"key": "browser_detection_brave", "value": False},
                    {
                        "key": "audio_codecs",
                        "value": '{"ogg":"probably","mp3":"probably","wav":"probably","m4a":"maybe","aac":"probably"}',
                    },
                    {
                        "key": "video_codecs",
                        "value": '{"ogg":"probably","h264":"probably","webm":"probably","mpeg4v":"","mpeg4a":"","theora":""}',
                    },
                    {"key": "media_query_dark_mode", "value": True},
                    {"key": "headless_browser_phantom", "value": False},
                    {"key": "headless_browser_selenium", "value": False},
                    {"key": "headless_browser_nightmare_js", "value": False},
                    {"key": "document__referrer", "value": ""},
                    {"key": "window__ancestor_origins", "value": ["https://bloxflip.com"]},
                    {"key": "window__tree_index", "value": [8]},
                    {
                        "key": "window__tree_structure",
                        "value": "[[],[],[],[],[],[],[[]],[],[]]",
                    },
                    {
                        "key": "window__location_href",
                        "value": "https://bloxflip.com/arkose_captcha2.html",
                    },
                    {
                        "key": "client_config__sitedata_location_href",
                        "value": "https://bloxflip.com/arkose_captcha2.html",
                    },
                    {
                        "key": "client_config__surl",
                        "value": "https://api.bloxflip.com//arkose-proxy",
                    },
                    {"key": "mobile_sdk__is_sdk"},
                    {"key": "client_config__language", "value": None},
                    {"key": "navigator_battery_charging", "value": True},
                    {"key": "audio_fingerprint", "value": random.uniform(124,125)},
                ],
            },
            {
                "key": "fe",
                "value": [
                    "DNT:unknown",
                    "L:en-US",
                    "D:24",
                    "PR:1",
                    "S:1920,1080",
                    "AS:1920,1032",
                    "TO:300",
                    "SS:true",
                    "LS:true",
                    "IDB:true",
                    "B:false",
                    "ODB:false",
                    "CPUC:unknown",
                    "PK:Win32",
                    f"CFP:{gen}"
                    "FR:false",
                    "FOS:false",
                    "FB:false",
                    "JSF:Arial,Arial Black,Arial Narrow,Calibri,Cambria,Cambria Math,Comic Sans MS,Consolas,Courier,Courier New,Georgia,Helvetica,Impact,Lucida Console,Lucida Sans Unicode,Microsoft Sans Serif,MS Gothic,MS PGothic,MS Sans Serif,MS Serif,Palatino Linotype,Segoe Print,Segoe Script,Segoe UI,Segoe UI Light,Segoe UI Semibold,Segoe UI Symbol,Tahoma,Times,Times New Roman,Trebuchet MS,Verdana,Wingdings",
                    "P:Chrome PDF Viewer,Chromium PDF Viewer,Microsoft Edge PDF Viewer,PDF Viewer,WebKit built-in PDF",
                    "T:0,false,false",
                    "H:6",
                    "SWF:false",
                ],
            },
            {"key": "ife_hash", "value": secrets.token_hex(16)},
            {"key": "cs", "value": 1},
            {
                "key": "jsbd",
                "value": '{"HL":3,"NCE":true,"DT":"Roblox","NWD":"false","DOTO":1,"DMTO":1}',
            },
        ]
        data = self.encrypt(json.dumps(the_data, separators=(',', ':')), key)
        return base64.b64encode(data.encode("utf-8")).decode("utf-8")
    def bloxflip_funcap_token(self,data):
        url = "https://api.bloxflip.com//arkose-proxy/fc/gt2/public_key/476068BF-9607-4799-B53D-966BE98E2B81"
        payload = {
            "bda": self.get_bda(),
            "public_key": "476068BF-9607-4799-B53D-966BE98E2B81",
            "site": "https://bloxflip.com",
            "userbrowser": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "rnd": random.random(),
            "data[blob]": data
        }

        headers = {
            'authority': 'api.bloxflip.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://bloxflip.com',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

        x = self.t.post(url, headers=headers, data=payload).json()
        try:
            return x['token']
        except:
            return x


# made by coxy.57
# made by coxy.57
# made by coxy.57
# made by coxy.57
# made by coxy.57
# made by coxy.57
# made by coxy.57


