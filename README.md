
# Microparticle-counting

# Microscopic video streams are used to count micro particles using detection and tracking algorithm

## Abstract

*Aparticle counting criterion is used to choose the
best focal length, where a best-quality video is considered to
have the maximum number of particles, with two methods,
background subtraction for detection and centroids differences
for tracking at first, after that, Hough Circles detection.


## See DEMO examples:

* <https://drive.google.com/drive/u/1/folders/1ahKUEzvxmJj1uRt2Uky9X1Vsl6TGsSdv>

## Introduction

*VFocal-length manual adjustment can be subject to human
error, for that, we are trying to find the best focal point of a
given video stream capturing microparticles flowing in a
chip, this chip that has a cross-sectional area of a rectangle
and it has three input tubes from one side, one tube for the
feed of microparticles-water mixture and the other two tubes
pump particles-free water that acts as focusing fluid, aiming
to focus the particles in one lateral space, experimentally
speaking, the flowing particles are not focused in one lateral
space, in fact, and with different observations, we found the
focused particles flow in a range of 100 Micro-meter across
the cross-sectional area of the chip. For that, we are
proposing two methods to find the lateral space that most
particles flow at, basically, these two methods to partially
automatize focal-length adjustment by counting the detected
and tracked microparticles in the given video, under the
assumption of the more we can count and detect particles in a
given video, the more In-Focus the particles are presented in
the frame.

## Figure to demonstrate
![alt text](https://github.com/martin-ss/Microparticle-counting/blob/main/DEMO-PARTICLES%20(1)%20(1)_072.jpg?raw=true)


  

## Table of contents




> * [About / Synopsis](#Abstract)
>   * [Table of contents](#table-of-contents)
>   * [Installation](#installation)
>   * [Usage](#usage)
>     * [Screenshot of the Environment](#screenshot-of-the-Environment)
>     
>     
>   * [Refrencess](#Refrencess)


>   * [About the Project](#)


## Installation

Sample:

* From the Crrent repo: git clone  https://github.com/martin-ss/Microparticle-counting

## Usage

* This project is aimed to Count micro particles using two different detection methods with tracking
### Result of the Different focal points using the different detection methods

![alt text](https://github.com/martin-ss/Microparticle-counting/blob/main/Figure%202021-03-07%20211641.png?raw=true)






## About The Project
It is impelemneted as a part of an introduction of a master-2 degree internship
