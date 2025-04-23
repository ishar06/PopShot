# **Basic Models of Artificial Neural Networks** 

---

### ✅ **Key Concepts:**

#### 🔹 **Single-layer Feed-forward Network:**
- Input is passed forward **in one direction** through the network.
- Consists of an **input layer** and an **output layer** (no hidden layers).
- **Each input neuron connects to all output neurons** via weighted links.

#### 🔹 **Input Layer:**
- **Receives raw data** like images, text, or numbers.
- Performs **data formatting** (e.g., normalization, flattening).
- **Passive**: No activation function or computation.
- **No trainable parameters** (weights/biases).

#### 🔹 **Weights:**
- Represent the **importance of each input**.
- Large weights = more influence on the output.
- **Learned and adjusted** during training via **backpropagation** to reduce the **loss function**.

---

### ✅ **Network Architectures:**

#### 🔹 **Multilayer Feed-forward Network:**
- **Input Layer** → **Hidden Layer(s)** → **Output Layer**.
- **Hidden layers**: Internal computation, not exposed externally.
- More hidden layers = More complex, possibly more efficient.

#### 🔹 **Fully Connected Network:**
- Every neuron in one layer is connected to **every neuron** in the next layer.

---

### ✅ **Feedback and Recurrent Networks:**

#### 🔹 **Feed-forward vs. Feedback:**
- **Feed-forward**: No cycles or loops.
- **Feedback**: Output is looped back as input to same/previous layers.

#### 🔹 **Types of Feedback:**
- **Lateral Feedback**: Output directed back to same-layer neurons.
- **Recurrent Networks**:
  - Include loops → **Retain information over time**.
  - Ideal for **sequential data** (e.g., time series, NLP).
  - Used in **speech recognition, language modeling**.

#### 🔹 **Single-layer Recurrent Network:**
- One layer with **feedback to itself** or others.

#### 🔹 **Multilayer Recurrent Network:**
- Feedback can go:
  - From **one layer to previous layers**,
  - Or **within the same layer**.

---

### ✅ **Competitive Learning & Maxnet:**

#### 🔹 **Maxnet:**
- Used for **Winner-Take-All (WTA)** selection.
- Each neuron:
  - **Excites itself**.
  - **Inhibits others** using a small negative weight (−ε).
- Repeated iterations → Only the **strongest neuron survives**.
- Used in applications requiring **dominant choice selection**.

---

### 📌 **Quick MCQ Points Recap:**
- Input layer: No computation, no weights, just data input.
- Feed-forward = No cycles; Feedback = Cycles exist.
- More hidden layers → More complexity.
- Weights determine feature importance.
- Recurrent networks → Work on sequential/time-based data.
- Maxnet → Used in competitive learning to pick strongest neuron.

---
---
---
# **Incremental (Online) Training** and **Batch (Offline) Training**:

---

### ✅ **Incremental Training / Online Training:**

- The network **updates its weights after every single training example**.
- **Each input → calculate output → compare with target → update weights immediately**.
- Learns one step at a time, good for real-time or streaming data.
- **Fast and easy to implement**, but can fluctuate more in learning.

🧠 **Think of it like learning after every question** in a quiz.

---

### ✅ **Batch Training / Offline Training:**

- The network sees the **entire training set (called an epoch)** first.
- Then it **calculates the average error** from all examples.
- Updates the weights **only once after the full pass**.
- **More stable**, but **takes more memory and time**.

🧠 **Think of it like studying all topics first, then correcting mistakes at once**.

---

### ⚖️ **Key Differences:**

| Feature                | Incremental Training           | Batch Training                |
|------------------------|--------------------------------|-------------------------------|
| Updates after...       | Each example                   | Whole dataset (epoch)         |
| Speed                  | Faster                         | Slower                        |
| Stability              | Less stable (fluctuates)       | More stable                   |
| Ideal for...           | Real-time, small datasets      | Large datasets, better accuracy |

---
---
---
# **Artificial Neural Networks (ANNs)**—great for MCQ revision or short-answer prep:

---

### 1️⃣ **What are the key components of an artificial neural network (ANN)?**

- **Neurons (Nodes):** Basic units that process input and generate output.
- **Layers:** 
  - **Input Layer** – receives raw data.
  - **Hidden Layer(s)** – do most of the processing.
  - **Output Layer** – gives final prediction.
- **Weights:** Determine the importance of inputs.
- **Biases:** Extra values added to shift the output.
- **Activation Functions:** Decide if a neuron should be activated.

---

### 2️⃣ **Explain the function of the input layer in an artificial neural network.**

- Takes raw input data (like images, text, or numbers).
- Passes the data to the next layer.
- **Does not perform calculations** or apply activation.
- No weights or biases—just acts as a **data carrier**.

---

### 3️⃣ **What role do weights play in the architecture of an ANN?**

- Weights decide how important each input is.
- Higher weight = more influence on the output.
- Adjusted during training to **minimize error/loss**.
- Core part of the learning process.

---

### 4️⃣ **How does the output layer differ from the hidden layers in an ANN?**

- **Output Layer:** Produces the final result/prediction.
- **Hidden Layers:** Intermediate processing, apply transformations to data.
- Output layer often uses specific activations (e.g., softmax for classification).

---

### 5️⃣ **What is a single-layer artificial neural network (ANN), and how does its architecture differ from a multi-layer neural network?**

- **Single-layer ANN:** Has only input and output layers.
  - Simple and faster.
  - Cannot solve complex problems.
- **Multi-layer ANN:** Has one or more hidden layers.
  - Can handle **non-linear** and **complex patterns**.

---

### 6️⃣ **How does a single-layer perceptron (SLP) work in terms of input, processing, and output?**

1. Takes multiple inputs.
2. Multiplies each by a weight and adds bias.
3. Passes result through an activation function.
4. **Produces one output** (e.g., 0 or 1 in binary classification).

---

### 7️⃣ **What is the role of weights and biases in a single-layer neural network?**

- **Weights:** Scale the importance of each input.
- **Bias:** Helps shift the activation function output.
- Together they help the network learn the correct mapping from input to output.

---

### 8️⃣ **How does the activation function influence the output of a single-layer ANN?**

- Introduces **non-linearity** to the output.
- Decides whether the neuron should be **"fired" (activated)** or not.
- Common examples: Sigmoid, ReLU, Step Function.
- Helps the model learn complex patterns.

---

### 9️⃣ **What are the limitations of a single-layer neural network in solving complex problems?**

- Can only solve **linearly separable** problems (e.g., AND, OR).
- Fails for **non-linear** problems (e.g., XOR).
- Lacks the depth to **extract complex features**.
- That’s why multi-layer networks (like deep learning) are preferred for real-world tasks.

---
---
---
# **Convolutional Neural Networks (CNNs)** 

---

### **What is a CNN?**
- **CNN (Convolutional Neural Network)** is a type of **feed-forward deep learning model** mainly used for **image processing** tasks.
- **Main Layers**:  
  🔹 **Input Layer**  
  🔹 **Convolutional Layer**  
  🔹 **Pooling Layer**  
  🔹 **Fully Connected Layer**  
  🔹 **Output Layer**

---

### **1. Input Layer**
- Takes in the **raw pixel values** of the image.
- Each image pixel is a value (e.g., grayscale or RGB).

---

### **2. Convolutional Layer**
- Contains **trainable filters (kernels)** that slide across the image.
- Each filter produces a **feature map** using dot products.
- Detects **visual patterns** like edges, shapes, textures.
- **Filter size**: Typically smaller than image (e.g., 3×3).
- **Output**: Set of 2D feature maps stacked into a volume.
- **Input shape**: `n × n × p` (e.g., 5×5 grayscale → p=1; RGB → p=3)
- **Filter shape**: `r × r × q`; result feature map size: `n − r + 1`.

#### 🧠 **Example:**
Applying a **3×3 edge detection kernel** over a **5×5 grayscale image**, results in a feature map by computing **dot products** region-wise.

---

### **3. Pooling Layer**
- Reduces **spatial size** of feature maps → **less computation**, prevents **overfitting**.
- Common method: **Max Pooling** (selects max value from region).
- Pooling size (e.g., 2×2), **Stride** defines sliding step.
- Output is a **smaller version** of input feature map, retaining important features.

#### 🧠 **Example:**
Apply **max pooling** over **2×2 regions**, output = max of each region.

---

### **4. Fully Connected Layer**
- After multiple conv + pooling layers, **flatten output** into a vector.
- Connects to standard neurons (like ANN).
- Combines features for **final prediction**.

---

### **5. Output Layer**
- Final prediction, e.g., **classification score**.
- Number of neurons = **number of output classes**.

---

### ✅ **Why CNNs are better than ANN for image tasks**
- **Automatically learn features** (edges, shapes, patterns) from raw images.
- **No need for manual feature extraction**.
- **Filters slide over image**, reducing parameters vs ANN.
- **Pooling layers** make CNNs **robust to spatial changes** (object position/rotation).
- **Efficient** and **scalable** for high-resolution images.

---
---
---
# **Recurrent Neural Networks (RNNs)**

---

### **What is an RNN?**
- **Recurrent Neural Network (RNN)** is a type of **neural network designed for sequential data**.
- It uses a **feedback mechanism** to maintain **hidden states (memory)** of previous inputs.
- **Connections form directed cycles**, enabling RNNs to **“remember” context** from past steps.
- Ideal for data types where **order and context matter**, such as **text, speech, time series, and video**.

---

### **How RNNs Work**
- **Information is fed back** into the system after each time step.
- Like reading a sentence: **each new word prediction depends on previous words**.
- The **output of one step becomes the input for the next**, allowing the network to **retain context**.

---

### **Recurrent Unit**
- **Core unit** of an RNN, holding a **hidden state**.
- Maintains **memory** by **feeding back the hidden state**.
- Captures **dependencies across time** in sequential data.

---

### **Unrolling (or Unfolding)**
- Represents the **recurrent structure over time**.
- Each step in the sequence is shown as a separate layer → easier to **visualize information flow**.

---

### **Backpropagation Through Time (BPTT)**
- Special version of backpropagation adapted for RNNs.
- **Errors are propagated through time** steps.
- Helps adjust weights to **learn long-term dependencies** in sequences.

---

### **Weight Sharing**
- Unlike traditional deep networks with separate weights per layer, **RNNs share weights** across time steps.
- This design allows **consistent learning across sequences** and reduces complexity.

---

### **Applications**
- **Natural Language Processing (NLP)**
- **Time Series Forecasting**
- **Music Generation**
- **Speech Recognition**
- **Video Captioning**

---
---
---
# **Radial Basis Function Network (RBFN)**:

---

**🔹 RBFN Overview:**  
An **RBFN is a type of neural network** used mainly for **classification** and **function approximation**. It uses **nonlinear activation functions**, most commonly the **Gaussian kernel**.

---

**🔹 Gaussian Kernel & Properties:**  
- **Gaussian functions** are radially symmetric, meaning the output depends only on the **distance** from a center, not the direction.  
- The output is **positive**, peaking at the center and approaching **zero as distance increases**.

---

**🔹 Architecture:**  
- **Two layers:**  
  - **Hidden layer:** Applies **radial basis (Gaussian)** functions.  
  - **Output layer:** Performs a **linear combination** of hidden layer outputs.  
- The hidden units respond **strongly only to inputs close to their center**, making the network behave like a **localized receptive field** system.

---

**🔹 Training Process:**  
1. **Initialize weights** randomly.  
2. For each input:  
   - Transmit input to hidden layer.  
   - **Compute the RBF** using Euclidean distance from centers.  
   - Select **centers and spread (σ)** from input vectors.  
   - Compute hidden and final **outputs using weighted sums**.  
3. **Adjust weights** based on error until the stopping condition is met.

> Training combines **unsupervised learning** for the hidden layer (selecting centers) and **supervised learning** for the output layer.

---

**🔹 Applications:**  
- **Pattern Recognition** (e.g., speech, image)  
- **Time Series Prediction**  
- **Adaptive Control Systems**  
- **Medical Diagnosis**

---
---
---
# **McCulloch–Pitts (M–P) Neuron**:

---

### 🔹 **What is it?**
The **McCulloch–Pitts neuron**, proposed in **1943**, is the **earliest model of an artificial neuron** used in neural networks. It's mainly used for simulating **simple logic functions**.

---

### 🔹 **Structure & Working:**
- **Inputs**: Divided into:
  - **Excitatory inputs** (positive weights)
  - **Inhibitory inputs** (negative weights)
- **Weights**: All excitatory inputs have the **same weight**, while inhibitory inputs suppress the neuron.
- **Threshold (Ө)**: A **fixed value**. If the net input exceeds this threshold, the neuron **fires** (outputs 1); otherwise, it **doesn’t** (outputs 0).
- **Binary output**: The neuron either **fires (1)** or **does not fire (0)** — no in-between.

---

### 🔹 **Key Firing Condition:**
- Neuron fires **only if**:
  - The **sum of excitatory inputs** is **≥ threshold**
  - **No inhibitory input** is active

> Example: If **k** excitatory inputs are active and **kw ≥ Ө**, the neuron fires.  
> If fewer than k are active or any inhibitory input is active, it won't fire.

---

### 🔹 **Inhibition Conditions:**
- **Weak absolute inhibition**: Total inhibitory effect must be considered.  
  - Condition: `Ө > nw - P`
- **Strong absolute inhibition**: Even a **single active inhibitor** blocks firing.  
  - Condition: `Ө > nw - Pmin`

---

### 🔹 **Training?**
- **No learning or training algorithm** exists.
- You **manually set weights and threshold** to implement **logic gates** like AND, OR, NOT.

---

### 🔹 **Applications:**
- Modeling **logic functions** in early neural networks
- Foundation for modern neural networks

---
---
---
# Hebb Network and Hebbian Learning Rule**:

---

### 🔹 **What is Hebb Network?**
- Proposed by **Donald Hebb in 1949**.
- Based on the principle: **"Neurons that fire together, wire together."**
- Strengthens connections between neurons **if they activate simultaneously**.

---

### 🔹 **Core Principle**
- If input neuron **x** and output neuron **y** are active **together**, increase the **weight (w)** between them.
- No significant change occurs if one fires and the other doesn’t.
- **Unsupervised learning** – No error or target output used.

---

### 🔹 **Weight Update Rule**
- **Mathematical form**:
  \[
  w_i = w_i + \eta \cdot x \cdot y
  \]
  where:
  - \( w_i \): weight
  - \( \eta \): learning rate
  - \( x \): input
  - \( y \): output

---

### 🔹 **Training Algorithm Steps**
1. **Initialize weights** to zero: \( w_i = 0 \)
2. For each input-output pair:
   - Set input: \( x_i = s_j \)
   - Set output: \( y = t \)
   - **Update weights**: \( w_i^{new} = w_i^{old} + x_i \cdot y \)
   - **Update bias**: \( b^{new} = b^{old} + y \)

---

### 🔹 **Vector Form Update**
- \[
  \Delta w = x \cdot y
  \]
- \[
  w_{new} = w_{old} + \Delta w
  \]

---

### 🔹 **Applications**
- **Pattern Association**
- **Pattern Classification**
- **Pattern Categorization**
- General **unsupervised learning tasks**

---

### 🔹 **Characteristics**
- Simple and biologically inspired
- No error correction involved
- Works best with **bipolar data** (values like -1, +1)
- Suitable for **associative learning tasks**

---

### 🔹 **Limitations**
- **Unbounded weight growth** if no normalization or decay
- Does **not decrease** weights even if input and output are anti-correlated
- Needs enhancement (e.g., **Oja’s rule**) for stability and practical use

---
---
---

