#define GLFW_INCLUDE_VULKAN
#include <GLFW/glfw3.h>
#include <iostream>
#include <vector>
#include <stdexcept>
#include <cstdlib>
#include <cstring>

// Include stb_image for loading images
#define STB_IMAGE_IMPLEMENTATION
#include "third_party/stb_image.h"

// Vulkan objects
VkInstance instance;
VkDevice device;
VkPhysicalDevice physicalDevice = VK_NULL_HANDLE;
VkQueue computeQueue;
VkCommandPool commandPool;
VkDescriptorSetLayout descriptorSetLayout;
VkDescriptorPool descriptorPool;
VkDescriptorSet descriptorSet;
VkPipelineLayout pipelineLayout;
VkPipeline computePipeline;
VkBuffer inputBuffer, outputBuffer;
VkDeviceMemory inputBufferMemory, outputBufferMemory;

// Basic error handling
void throwError(const char* msg) {
    throw std::runtime_error(msg);
}

// Create Vulkan instance
void createInstance() {
    VkApplicationInfo appInfo = {};
    appInfo.sType = VK_STRUCTURE_TYPE_APPLICATION_INFO;
    appInfo.pApplicationName = "Compute Shader with SSBO";
    appInfo.applicationVersion = VK_MAKE_VERSION(1, 0, 0);
    appInfo.pEngineName = "No Engine";
    appInfo.engineVersion = VK_MAKE_VERSION(1, 0, 0);
    appInfo.apiVersion = VK_API_VERSION_1_2;

    VkInstanceCreateInfo createInfo = {};
    createInfo.sType = VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO;
    createInfo.pApplicationInfo = &appInfo;

    if (vkCreateInstance(&createInfo, nullptr, &instance) != VK_SUCCESS) {
        throwError("failed to create Vulkan instance!");
    }
}

// Find a suitable physical device (GPU)
void pickPhysicalDevice() {
    uint32_t deviceCount = 0;
    vkEnumeratePhysicalDevices(instance, &deviceCount, nullptr);
    if (deviceCount == 0) {
        throwError("failed to find GPUs with Vulkan support!");
    }

    std::vector<VkPhysicalDevice> devices(deviceCount);
    vkEnumeratePhysicalDevices(instance, &deviceCount, devices.data());
    physicalDevice = devices[0]; // Just pick the first device for simplicity
}

// Create logical device and queue
void createDevice() {
    VkDeviceQueueCreateInfo queueCreateInfo = {};
    queueCreateInfo.sType = VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO;
    queueCreateInfo.queueFamilyIndex = 0; // Compute queue family (adjust accordingly)
    queueCreateInfo.queueCount = 1;
    float queuePriority = 1.0f;
    queueCreateInfo.pQueuePriorities = &queuePriority;

    VkDeviceCreateInfo createInfo = {};
    createInfo.sType = VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO;
    createInfo.pQueueCreateInfos = &queueCreateInfo;
    createInfo.queueCreateInfoCount = 1;

    if (vkCreateDevice(physicalDevice, &createInfo, nullptr, &device) != VK_SUCCESS) {
        throwError("failed to create Vulkan logical device!");
    }

    vkGetDeviceQueue(device, 0, 0, &computeQueue);
}

// Helper function to create a Vulkan buffer
void createBuffer(VkBuffer& buffer, VkDeviceMemory& bufferMemory, VkDeviceSize size, VkBufferUsageFlags usage) {
    VkBufferCreateInfo bufferCreateInfo = {};
    bufferCreateInfo.sType = VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO;
    bufferCreateInfo.size = size;
    bufferCreateInfo.usage = usage;
    bufferCreateInfo.sharingMode = VK_SHARING_MODE_EXCLUSIVE;

    if (vkCreateBuffer(device, &bufferCreateInfo, nullptr, &buffer) != VK_SUCCESS) {
        throwError("failed to create buffer!");
    }

    VkMemoryRequirements memRequirements;
    vkGetBufferMemoryRequirements(device, buffer, &memRequirements);

    VkMemoryAllocateInfo allocInfo = {};
    allocInfo.sType = VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO;
    allocInfo.allocationSize = memRequirements.size;
    allocInfo.memoryTypeIndex = 0; // Memory type index (find suitable one)

    if (vkAllocateMemory(device, &allocInfo, nullptr, &bufferMemory) != VK_SUCCESS) {
        throwError("failed to allocate buffer memory!");
    }

    vkBindBufferMemory(device, buffer, bufferMemory, 0);
}

// Compile shader code (in practice, you'll use a separate tool for this)
// Use Vulkan's SPIR-V compiler (glslangValidator) to compile the shader
void compileShader() {
    // This function should run the glslangValidator tool to compile .comp -> .spv
    // For simplicity, assume compute_shader.spv is precompiled.
}

// Main function
int main() {
    try {
        createInstance();
        pickPhysicalDevice();
        createDevice();

        compileShader(); // Compile your compute shader (see comments below)

        // Create SSBO buffers
        VkDeviceSize bufferSize = sizeof(float) * 1024;
        createBuffer(inputBuffer, inputBufferMemory, bufferSize, VK_BUFFER_USAGE_STORAGE_BUFFER_BIT);
        createBuffer(outputBuffer, outputBufferMemory, bufferSize, VK_BUFFER_USAGE_STORAGE_BUFFER_BIT);

        // Create other Vulkan objects (descriptor set, pipeline, etc.)

        // Run compute shader
        // 1. Dispatch work to the GPU
        // 2. Synchronize and retrieve results

        // Clean up Vulkan resources

    } catch (const std::exception& e) {
        std::cerr << "Vulkan setup failed: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
