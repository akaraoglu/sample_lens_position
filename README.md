# Introduction

Focusing in imaging, particularly in photography and videography, is the process of adjusting the optical system so that the image of an object comes into sharp view on the imaging sensor. This is crucial because the quality of focus directly affects the clarity and detail of the resulting image, influencing both the aesthetic and technical aspects of the final output.

## Importance of Focusing
The primary goal of focusing is to ensure that the subject of the image is rendered with maximum sharpness. Whether manually or through autofocus systems, achieving correct focus is essential for capturing images that are visually appealing and effectively communicate the photographer's intent. In scenarios ranging from macro photography to landscape and portrait photography, proper focus determines whether the details necessary for the image's impact are adequately captured.

## Basic Principles and Formulas
Focusing involves several key concepts and mathematical formulas that help photographers and engineers design systems and techniques for optimal image capture:

## 1) Thin-Lens Equation
The Thin-Lens Equation is a fundamental principle in optics that describes the relationship between the focal length of a lens, the distance from the lens to the object being focused on, and the distance from the lens to the image formed by that object. It applies to lenses that are thin enough that their thickness can be neglected in calculations, a common approximation in many practical situations.

![image](https://github.com/akaraoglu/focus_bracketing/assets/32932292/a2b78741-056f-49a3-9f22-2198834f6e40)

The formula for the **Thin-Lens Equation** is:

![image](https://github.com/akaraoglu/focus_bracketing/assets/32932292/103611d3-4324-4213-bcd5-675291f8aa9a)
  
Where 𝑓 is the focal length, 𝑑𝑜 is the distance to the object, and 𝑑𝑖 is the distance to the image plane (sensor). This fundamental formula helps determine where the lens should be focused for a clear image of an object at a given distance.

## 2) Circle of Confusion
The Circle of Confusion (CoC) refers to the optical spot created by a cone of light from a lens that is not perfectly focused. In simpler terms, it is the degree to which a point light source appears as a blurred, disc-like shape in an image, which affects image sharpness. CoC is a critical concept in understanding optical imaging, particularly in photography and cinematography. It represents the maximum blur spot that is indistinguishable from a point to the human eye or is considered acceptably sharp in an image. CoC is influenced by sensor size, viewing conditions, and print size.

![image](https://github.com/akaraoglu/focus_bracketing/assets/32932292/49cb8111-79c5-46c3-ad82-cd2a2046ee9a)

The Circle of Confusion can be calculated based on sensor size and desired print resolution. A commonly used formula to estimate CoC is:

![image](https://github.com/akaraoglu/focus_bracketing/assets/32932292/8e7363d8-ec5d-4db5-bff2-e64998a37e14)

Where:

- 𝑑 is the diagonal of the sensor in millimeters.
- 1730 is a constant that comes from typical viewing conditions and visual acuity assumptions (Print Size / Image Size)  (this constant can vary depending on the source, with some using 1500 to 2000 based on more critical sharpness criteria).

## 3) Hyperfocal Distance
Hyperfocal distance is the closest distance at which a lens can be focused while keeping objects at infinity acceptably sharp; focusing at this distance maximizes the depth of field from half this distance to infinity.

**Hyperfocal Distance Formula** 𝐻 can be calculated using the formula:

![image](https://github.com/akaraoglu/focus_bracketing/assets/32932292/f188ad17-02ee-46e1-ada8-5bf356a37323)

Where:

- 𝑓 is the focal length of the lens,
- 𝑁 is the aperture number (f-stop),
- 𝑐 is the Circle of Confusion.

By focusing on the hyperfocal distance, photographers can achieve the deepest possible depth of field for a given aperture and focal length. The near and far focus limits are particularly useful for landscape photographers who need to ensure maximum sharpness from the foreground to the horizon. Understanding and calculating these distances allows photographers to pre-plan their shots for optimal sharpness across the entire image.

## 4) Depth of Field Explained
Depth of Field (DoF) is the range within a photo that appears acceptably sharp. It is influenced by the lens aperture, the focal length, the focus distance, and the size of the Circle of Confusion. It is the range from near focus distance to far focus distance. The formula for calculating DoF is given by:

![image](https://github.com/akaraoglu/focus_bracketing/assets/32932292/d1bdbccc-7f37-452e-890f-d6a9a4d791c5)

Where:

- 𝑢 is the distance to the subject,
- 𝑁 is the aperture number,
- 𝑐 is the Circle of Confusion,
- 𝑓 is the focal length.
 
The "+/-" in the formula accounts for the DoF extending beyond and in front of the subject.


## 5) Limits of acceptable sharpness
### Near Focus and Far Focus Distance Limits
The near focus and far focus distance limits define the boundaries within which all objects are rendered acceptably sharp in an image.

**Near Focus Distance Limit**  𝐷𝑛  can be determined by:

![image](https://github.com/akaraoglu/focus_bracketing/assets/32932292/21a93472-e703-4029-9a75-c0374c6bb2e6)

Where:

- 𝑠 is the focus distance,
- 𝐻 is the hyperfocal distance,
- 𝑓 is the focal length.

**Far Focus Distance Limit** 𝐷𝑓 is calculated as:

![image](https://github.com/akaraoglu/focus_bracketing/assets/32932292/b1c13259-416a-493c-ae78-d8774e33b60a)

If 𝑠 is greater than 𝐻, then 𝐷𝑓 is infinity.

## 6) AutoFocus Systems
Autofocus (AF) systems are designed to automatically adjust the camera lens to achieve clear, sharp images of subjects by focusing the lens correctly without manual intervention. These systems are essential components in many modern cameras, including DSLRs, mirrorless cameras, and smartphones, providing convenience and speed that are critical in various photography scenarios.
Autofocus systems operate by receiving data from the lens and the sensor, processing this data through an autofocus algorithm, and then directing motor systems in the lens to adjust the focus elements until the subject is in focus. These systems can operate in single-shot modes, where focus is achieved once when the shutter button is partially pressed, or in continuous modes, which constantly adjust focus as long as the shutter button is held partially down or until the photo is taken.

### Types of Autofocus Systems

#### Active Autofocus Systems
Active autofocus systems determine the distance to the subject using techniques that involve projecting something (like infrared or ultrasonic signals) onto the subject and measuring how long it takes for the reflection to return.

How It Works: Active AF systems emit energy (light or sound) towards the subject. They then calculate the distance based on the time it takes for the energy to bounce back or based on the angle of the returning energy.
Advantages:
Works well in low light and can achieve focus even in complete darkness.
Less dependent on the contrast of the subject, making it effective in scenarios where passive systems might struggle.
Disadvantages:
The range is often limited, making it less effective for distant subjects.
Can be less accurate than optical methods because the signal might not reflect directly back or might scatter, especially in complex environments.
Typical Uses: Commonly found in video cameras and some compact digital cameras. It's also used in smartphones, particularly for video autofocus because of its robustness in diverse lighting conditions.
Passive Autofocus Systems
Passive autofocus systems rely on the analysis of the image formed by the actual camera lens without emitting any type of signal towards the subject. This category includes both phase detection and contrast detection autofocus systems.

How It Works:
Phase Detection: Uses a special sensor to split incoming light into pairs, comparing them to determine focus. This method measures the phase of the light waves to quickly determine focus adjustment.
Contrast Detection: Analyzes the contrast in the image captured by the main image sensor by shifting the lens and determining the point of highest contrast, which correlates to the sharpest focus.
Advantages:
Does not require emitting any signals, making it unobtrusive.
Typically offers higher accuracy and finer focus, especially useful in high-resolution photography.
Disadvantages:
Contrast detection can be slower, especially in low light.
Phase detection requires a certain amount of light and contrast to function effectively.
Typical Uses: DSLRs predominantly use phase detection, while mirrorless cameras and compact cameras often use contrast detection.
Hybrid Autofocus Systems
Hybrid autofocus systems combine elements of both active and passive systems, often integrating phase and contrast detection methods to optimize both speed and accuracy.

How It Works: Utilizes the speed of phase detection to quickly get near focus and then employs contrast detection to fine-tune the focus for precision.
Advantages:
Offers fast autofocus with high accuracy.
Effective in a wide range of lighting conditions.
Disadvantages:
More complex and potentially more expensive to implement.
Can still struggle in extreme conditions such as very low light or very fast-moving subjects.
Typical Uses: Many modern mirrorless cameras, high-end compact cameras, and advanced smartphones use hybrid autofocus systems to leverage the strengths of both active and passive methods for superior performance.
Each type of autofocus system has its own set of strengths and weaknesses, making them suitable for different applications and conditions. The choice between active, passive, and hybrid autofocus systems depends on factors like lighting conditions, subject movement, and the specific needs of the photographer or videographer.


## 7) Focus Bracketing 
Focus bracketing is an advanced photography technique used to extend the depth of field in images. It involves taking several photographs of the same scene at different focus distances and combining them to create a single image with greater sharpness throughout. To fully understand focus bracketing, we must first grasp the concept of the Circle of Confusion (CoC).

In focus bracketing, a photographer takes multiple shots of the same scene, adjusting the focus point slightly between each shot. This technique is particularly useful in macro photography where DoF is extremely shallow, even at small aperture settings.

The process involves determining the nearest and farthest points in the scene that need to be in focus. By using the DoF formula, one can calculate the necessary number of shots and the focus adjustment needed between each shot to ensure every part of the scene is sharp.

## Conclusion
Focus bracketing is a powerful technique that requires an understanding of both the Circle of Confusion and Depth of Field. By mastering these concepts and applying the correct formulas, photographers can create images with unprecedented depth and sharpness. This method is particularly useful in situations where traditional photography might fail to capture the complexity of a scene in sharp detail.

# 
# 
# 

# Circle of Confusion (CoC) Detailed in Digital Imaging
## What is Circle of Confusion?
In photography and optics, the Circle of Confusion (CoC) refers to the size of a blurred spot which results when a point source of light is not perfectly focused on a sensor or film plane. In the context of digital imaging, it's particularly significant because it helps define the limits of depth of field and overall image sharpness.

## CoC and Pixel Limitation
In digital cameras, the sensor is composed of pixels, which are the smallest units of an image capable of capturing light. The idea that one pixel can be the limit for the CoC comes from a desire for maximum resolution and sharpness; ideally, each point of light would map perfectly to a single pixel. However, if the CoC is smaller than a single pixel, the camera's resolving power is not fully utilized—the image can appear overly sharp or unnaturally detailed.

Conversely, if the CoC is larger than a single pixel, the resulting image starts losing detail and appears blurry because the blur circle spreads across multiple pixels, blending light and color information. This loss of detail usually manifests as a lack of clarity and contrast, especially noticeable in areas of fine texture or at the edges between different objects.

## Impact of Demosaicing on CoC
Demosaicing is a process used to reconstruct a full-color image from the incomplete color samples output by an image sensor overlaid with a color filter array (CFA). Most digital cameras use a Bayer filter matrix to capture color data, which only records one primary color per pixel. Demosaicing algorithms work to interpolate the two colors not captured at each pixel, predicting them from neighboring pixels.

The process of demosaicing has a direct impact on the perceived CoC because it introduces a level of softness or blur to the image. This is due to the interpolation needed to estimate missing color information, which can slightly enlarge the effective CoC. If CoC calculations do not consider the softening effects of demosaicing, the image may end up appearing less sharp than intended.

## Why CoC is Usually Tuned to 2 Pixels
The industry standard of tuning the Circle of Confusion to around 2 pixels is based on a balance between achievable detail and the inherent limitations of digital sensors and lens optics. By setting the CoC to approximately 2 pixels:

- **Resolution Optimization:** It ensures that the sensor resolves detail up to its practical limit without introducing unnecessary artifacts from trying to over-resolve beyond the sensor's capability or the resolving power of the lens.
- **Perceptual Sharpness:** This setting helps maintain a visually pleasing level of sharpness that aligns with human perception. Images are sharp enough to appear detailed without the harshness that can come from smaller CoC values.
- **Practicality in Lens Design:** Lenses are designed considering these standard CoC values, balancing sharpness, aberrations, and cost.

**In conclusion**, the choice of a CoC of around 2 pixels is a pragmatic decision that helps maximize both the technical and perceptual qualities of digital images. It accommodates the limitations and capabilities of current digital imaging technology while providing a good compromise between sharpness and natural-looking images.


# Appendix
## A schematic diagram of camera system

![image](https://github.com/akaraoglu/focus_bracketing/assets/32932292/b08f9e4a-d27a-4df8-b83f-c17c02649ee2)

![image](https://github.com/akaraoglu/focus_bracketing/assets/32932292/e1853512-8297-48da-9470-e1391eed1f53)


**Hyperfocal distance:** The closest distance at which a lens can be focused while keeping objects at infinity acceptably sharp. When the lens is focused at this distance, all objects at distances from half of the hyperfocal distance out to infinity will be acceptably sharp.
**Hyperfocal near limit:** The distance between the camera and the first element that is considered to be acceptably sharp when focusing at the hyperfocal distance. 
**Depth of field (DOF):** The distance between the farthest and nearest points which are in acceptable focus. This can also be identified as the zone of acceptable sharpness in front of and behind the subject to which the lens is focused on. 
**DOF near limit:** The distance between the camera and the first element that is considered to be acceptably sharp.
**DOF far limit:** The distance between the camera and the furthest element that is considered to be acceptably sharp.
**Depth of Field (DOF) In Front:** Distance between the DoF Near Limit and the focus plane.
**Depth of Field (DOF) Behind:** Distance between the focus plane and the DoF Far Limit.
