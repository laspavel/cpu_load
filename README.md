# CPU Load Generator

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)

A cross-platform CPU load generator for benchmarking and testing  
Supports configurable utilization, duration, and number of cores.

## 📌 Features

* Generate custom CPU load (1%–100%)
* Control test duration (in seconds)
* Load specific number of CPU cores
* Clean interruption handling (Ctrl+C)

## ⚙️ Requirements

- Python 3.6 or newer
- Linux, Windows

## 🚀 Installation & Usage

```bash
git clone https://github.com/laspavel/cpu_load.git
cd cpu_load
chmod +x cpu_load.py
./cpu_load.py [-i INTERVAL] [-u UTILIZATION] [-c CPUS] [-v]
```

Python dependencies are only from the standard library, no installation of packages is required.

Parameters:

| Parameters         | Description                                           |  Default             |
| ------------------ | ----------------------------------------------------- |  --------------------|
| -i, --interval     | Duration in seconds to run the test                   |  30                  |
| -u, --utilization  | CPU load percentage per core                          |  50                  |
| -c, --cpus         | Number of CPU cores to load  (max = physical cores)   |  all available cores |
| -v, --version      | Show program version and exit	                       |                      |

## 🧩  Example Usage

```bash
./load_cpu.py -i 60 -u 90 -c 2   # Run for 60 seconds at 90% load on 2 CPU cores
```

## 🛠 Build Standalone Binary

```bash
./build.sh
```

## 🧪 Testing Locally

If you prefer to run the load script directly on your host system:​

```bash
chmod +x load_cpu.sh
./load_cpu.py
```

⚠️ Make sure Python 3 is installed and executable is marked with `chmod +x`.

## 📁 Project Structure
```plaintext
cpu_load/
├── cron/                   # Example cron tasks for automated stress tests
├── src/                    # Source code for load generation
├── build.sh                # Script to build binary file
├── Dockerfile.build        # Docker image for build binary file
├── LICENSE                 # MIT License
└── README.md               # Project documentation
```

## 📄 License
MIT License.​

## 🤝 Contributions

Suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## 📬 Contact

Author: [laspavel](https://github.com/laspavel)

Feel free to reach out with questions or ideas.

---
