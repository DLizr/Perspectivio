#version 330

layout(location = 0) in vec3 position;
layout(location = 1) in vec3 color;

out vec3 fragmentColor;

uniform mat4 MVP;  // Actually PVM

void main() {
    gl_Position = MVP * vec4(position, 1.0);
    fragmentColor = color;
}