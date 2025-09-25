# Iris-Image-Recognition
**Overview**

This is a Python-based Iris Recognition System for secure biometric authentication. The system uses image preprocessing, iris segmentation, Haar wavelet feature extraction, and XOR-based matching to identify users based on their iris patterns.

It supports Admin-controlled enrollment and updates, user-only matching, and has a retry safeguard for security.

**Features**

- `Admin Registration:` Only one admin can be registered to control enrollment and updates.

- `User Enrollment:` Admin can add new users with their iris images.

- `Iris Update:` Admin can update the stored iris for existing users.

- `Iris Matching:` Any user can match an iris image against the database.

- `Security:` Maximum 3 failed match attempts trigger a "Contact Admin" message.

- `Format Validation:` Supports .jpg, .jpeg, .png images.

- `Lightweight:` Uses opencv-python-headless, numpy, and scikit-image.

**Project_structure**
```pgsql
iris_recognition/
│── main.py                  # Entry point CLI
│── admin.py                 # Admin registration, add/update users
│── database.py              # DB handling (JSON storage)
│── features.py              # Iris segmentation and feature extraction
│── matcher.py               # XOR-based iris matching
│── utils.py                 # Image validation and utility functions
│── requirements.txt         # Python dependencies
│── data/                    # Sample iris images
│── db.json                  # Database (auto-generated)
```
**Installation**
1. Clone the Repo
```bash
git clone <repo-url>
cd iris_recognition
```
2. Create a virtual environment (optional but recommended):
```bash
python -m venv iris_env
source iris_env/bin/activate   # Linux/macOS
iris_env\Scripts\activate      # Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
**Usage**
1. Register Admin (First Time)
```bash
python main.py --register-admin --username admin --password 1234
```
2. Add New User (Admin Only)
```bash
python main.py --add --user-id USER001 --username admin --password 1234 --image data/user1.jpg
```
3. Update User Iris (Admin Only)
```bash
python main.py --update --user-id USER001 --username admin --password 1234 --image data/new_user1.jpg
```
4. Match Iris (Anyone)
```bash
python main.py --match --image data/test1.jpg
```
>If a user fails 3 consecutive matches, the system outputs:
`Maximum retries reached. Contact Admin.`

**How it Works**
1. Image Validation: Accepts .jpg/.jpeg/.png images.
2. Iris Segmentation: Detects the iris using edge detection and circular Hough Transform.
3. Feature Extraction: Uses Haar wavelet transform, converts to binary iris code.
4. Database Management: Admin controls user iris records stored in db.json.
5. Matching: XOR of input iris code vs stored codes; minimum distance match selected.

Dependencies

1. Python 3.10+
2. opencv-python-headless
3. numpy
4. scikit-image

**Install with:**
```bash
pip install -r requirements.txt
```

**Future Scope**
- Integrate CNN-based iris feature extraction for higher accuracy.
- Real-time camera capture for enrollment and matching.
- Add GUI with Tkinter or PyQt for more interactive usage.
- Extend to multi-user systems with logging and audit trail.