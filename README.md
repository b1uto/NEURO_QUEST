Real-Time Adaptive AI in VR Gaming Through Heart Rate Monitoring

📖 Overview

This project explores how real-time physiological feedback can be used to enhance immersion in Virtual Reality (VR) games. Using a Polar H10 heart rate monitor and Unreal Engine, enemy AI dynamically adapts its behavior based on the player’s current heart rate, creating a responsive and personalized gameplay experience.

When the heart rate increases (stress/fear/excitement), enemies become more aggressive.

When the heart rate decreases (calm/control), enemies act more passively.

This creates a dynamic difficulty adjustment (DDA) system that mirrors the player’s physiological state, blurring the line between real-world responses and in-game experiences.

🎮 Features

Heart Rate Integration via Polar H10 + Pulsoid API.

Custom Python script (Selenium + WebSocket) to stream heart rate data into Unreal Engine.

AI Behavior Tree with 3 adaptive states:

Passive / Investigative (< 80 bpm)

Light Attack (80–100 bpm)

Heavy Attack (> 100 bpm)

AI Hearing Perception System that responds to player-generated noise.

Near real-time responsiveness (<1s latency) from heart rate to AI adaptation.

⚙️ Tech Stack

Engine: Unreal Engine 5.4

Language: C++ & Blueprints

External Integration: Python (Selenium, WebSocket, JSON)

Hardware: Polar H10 Heart Rate Monitor

Third-Party Tools/Assets: Pulsoid API, Mixamo Animations, Infinity Blade: GrassLands

📂 Project Workflow

Heart Rate Capture – Polar H10 via Pulsoid widget.

Python Processing – Heart rate scraped, serialized to JSON, sent via WebSocket.

Unreal Engine Receiver – JSON deserialized, passed to Enemy AI Controller.

Behavior Tree Updates – AI shifts states based on real-time thresholds.

Gameplay Response – Enemies dynamically adapt difficulty to mirror the player’s physiology.

🧪 Evaluation

Heart rate captured every second for continuous feedback.

Data transmitted with minimal latency using WebSockets.

AI transitions tested iteratively to ensure smooth difficulty shifts.

🔐 Ethical & Data Considerations

Privacy & Consent: Heart rate data is personal; informed consent required.

Security: WebSocket connections should be encrypted; no long-term storage of physiological data.

Accessibility: Alternative modes should be offered for players without HR monitors.

📚 References

Key supporting works:

Sekhavat (2017) – Heart rate monitoring & adaptive AI in games.

Saposnik et al. (2010) – Biofeedback in VR for rehabilitation.

Ravaja et al. (2006) – Emotional states linked to HR in gaming.

Yannakakis & Hallam (2009) – Dynamic Difficulty Adjustment via biofeedback.

Nacke et al. (2011) – Physiological feedback in game immersion.

(Full reference list in dissertation.)

🚀 Future Work

Incorporating additional biofeedback metrics (e.g., skin conductivity, breathing rate).

Expanding AI behavior repertoire for richer, more complex responses.

Optimizing for VR sword-combat mechanics initially scoped but excluded.

📜 Disclaimer

This is a student project developed as part of MSc Game Development (Programming) at Kingston University. No warranties are expressed or implied.
