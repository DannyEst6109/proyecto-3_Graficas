# GLSL

vertex_shader = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float tiempo;
uniform float valor;
uniform vec3 pointLight;
out vec3 outColor;
out vec2 outTexCoords;
void main()
{
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    float intensity = dot(modelMatrix * norm, normalize(light - pos));
    gl_Position = projectionMatrix * viewMatrix * pos;
    outColor = vec3(1.0,1.0 - valor * 2,1.0-valor * 2) * intensity;
    outTexCoords = texCoords;
}
"""
toon_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
in float outIntensity;
uniform sampler2D tex;
in vec2 outTexCoords;
in vec3 outColor;


void main()
{
    float curIntensity;
    if (outIntensity > 0.7){
        curIntensity = 0.7;
    }else if (outIntensity > 0.5){
        curIntensity = 0.5;
    }else if (outIntensity > 0.3){
        curIntensity = 0.3;
    }else {
        curIntensity = 0.1;
    }
    fragColor = (curIntensity * 4) * vec4(outColor,2) * texture(tex, outTexCoords) ;
}
"""


fragment_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
in vec3 outColor;
in vec2 outTexCoords;
uniform sampler2D tex;
void main()
{
    fragColor = vec4(outColor, 1) * texture(tex, outTexCoords);
}
"""

vertex_general = """
#version 450
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 texCoords;
uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;
uniform float valor;
uniform vec3 pointLight;
out vec3 outColor;
out vec2 outTexCoords;
out float outIntensity;
void main()
{
    vec4 norm = vec4(normal, 0.0);
    vec4 pos = vec4(position, 1.0) + norm * valor;
    pos = modelMatrix * pos;
    vec4 light = vec4(pointLight, 1.0);
    gl_Position = projectionMatrix * viewMatrix * pos;
    outTexCoords = texCoords;
    outColor = vec3(1.0,1.0 + valor * 2,1.0 + valor * 2);
    outIntensity = dot(modelMatrix * norm, normalize(pos - light));
}
"""


guate_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
// in vec3 outColor;
in vec2 outTexCoords;
in float outIntensity;
uniform sampler2D tex;
void main()
{
    vec3 color;
    float curIntensity;
    curIntensity = 0.9;
    if (outIntensity > 0.6){
        color = vec3(0, 0.64, 0.88);
        
    }else if (outIntensity > 0.4){
        color = vec3(1 , 1, 1);
        
    }else if (outIntensity > 0.1){
        color = vec3(0, 0.64, 0.88);
        
    }else {
        color = vec3(0.99, 0.88, 0.61);
        
    }
    ;
    fragColor = vec4(color, 2) * texture(tex, outTexCoords) * (outIntensity * 4) * (curIntensity * 4);
}
"""

lithuania_shader = """
#version 450
layout (location = 0) out vec4 fragColor;
// in vec3 outColor;
in vec2 outTexCoords;
in float outIntensity;
uniform sampler2D tex;
void main()
{
    vec3 color;
    float curIntensity;
    curIntensity = 0.9;
    if (outIntensity > 0.6){
        color = vec3(1, 0.72, 0.11);
        curIntensity = 0.5;
    }else if (outIntensity > 0.4){
        color = vec3(0,0.41, 0.22);
        curIntensity = 0.7;
    }else if (outIntensity > 0.1){
        color = vec3(0.74, 0.23, 0.20);
        curIntensity = 0.8;
    }else {
        color = vec3(0,0.41, 0.22);
        curIntensity = 0.7;
    }
    ;
    fragColor = (outIntensity * 3) * vec4(color, 2) * texture(tex, outTexCoords) * (curIntensity * 8);
}
"""

