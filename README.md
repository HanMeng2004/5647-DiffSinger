# Guideline for Easy Multi-DiffSinger

This is the final project for CS5647. Please note that, for the time being, we only offer support for Mandarin Chinese.

The model's name is Easy Multi-DiffSinger, which gives a preprocessing module of DiffSinger and enable it for multi-singer scenarios. The preprocessing module outline is shown here:

<img src="https://i.ibb.co/HB6XKbs/Screenshot-2023-11-01-at-12-49-21-AM.png" alt="arch-overview" style="zoom: 60%;" />

How to use it:

1. Copy and paste the following command in Anacoda Powershell Prompt to create a Python 3.8 virtual environment named diffsinger and activate the environment:

```bash
conda create -n diffsinger python=3.8 -y
conda activate diffsinger
```

2. Copy and paste the following code in Anacoda Powershell Prompt and press Enter to install dependencies:

```bash
pip install -r requirements.txt
```

3. Use the `cd` command in Anacoda Powershell Prompt to enter your DiffSinger-main repository:

```bash
cd path/to/your/DiffSinger-main
```

4. Run the following command to train on the existed dataset:

```bash
python scripts/train.py --config my_config.yaml --exp_name test_multi --reset
```

Here, please refer to the [schema](https://github.com/openvpi/DiffSinger/blob/main/docs/ConfigurationSchemas.md) to make modifications to the `my_config.yaml` file. Please replace `test_multi` with your model name for training.

5.  Run the following command to inference on your audio file and lyrics:

```bash
python preprocess/main.py 
```

You can find several example WAV, MIDI, and lyrics files under the `preprocess` folder. You can just visit our website demo to upload your files. However, if you wish to preprocess your files and infer via the command line, please follow these steps:

- [ ] Replace `houlai.wav` with the directory of your own `.wav` audio file.
- [ ] Replace `audio_output/preprocess/houlai_vocals.wav` with the directory of your `.wav` audio file after the separation process.
- [ ] Replace `/home/hanmeng/DiffSinger/preprocess` with your desired output directory.
- [ ] Replace `lyrics.txt` with the directory of your lyrics file.

For the inference script:

- [ ] Replace `samples/houlai.ds` with the directory of your `.ds` file.
- [ ] Replace `test_multi` with the name of your model.
- [ ] Replace `opencpop` with the name of the singer.
- [ ] Replace `output/houlai` with your preferred output directory.

These modifications will allow you to use the command line for preprocessing.

6. Run the following command to inference on your music scores without **preprocessing module**:

```bash
python scripts/infer.py acoustic samples/xiaoyaoxian.ds --exp test_multi --spk opencpop --out zaijian/xiaoyaoxian
```

Apart from using the preprocessing module, if you have already had a `.ds` file, you can use it with the `infer.py` scripts. Please make the following modifications:

- [ ] Replace `samples/xiaoyaoxian.ds` with the directory of your `.ds` file.
- [ ] Replace `test_multi` with the name of your model.
- [ ] Replace `opencpop` with the name of the singer.
- [ ] Replace `zaijian/xiaoyaoxian` with your preferred output directory.

The configs are:

```bash
Options:
  --exp EXP          Selection of model  [required]
  --ckpt STEPS       Selection of checkpoint training steps
  --spk TEXT         Speaker name or mix of speakers, now we support opencpop, man1 and man2
  --out DIR          Path of the output folder
  --title TEXT       Title of output file
  --num INTEGER      Number of runs
  --key INTEGER      Key transition of pitch
  --gender FLOAT     Formant shifting (gender control)
  --seed INTEGER     Random seed of the inference
  --depth INTEGER    Shallow diffusion depth
  --speedup INTEGER  Diffusion acceleration ratio
  --mel              Save intermediate mel format instead of waveform
  --help             Show this message and exit.
```

The original DiffSinger README.md content is as below.

If you are interested in creating your own dataset, please refer to the original documentation for detailed instructions and additional information.

# DiffSinger (OpenVPI maintained version)

[![arXiv](https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg)](https://arxiv.org/abs/2105.02446)
[![downloads](https://img.shields.io/github/downloads/openvpi/DiffSinger/total.svg)](https://github.com/openvpi/DiffSinger/releases)
[![Bilibili](https://img.shields.io/badge/Bilibili-Demo-blue)](https://www.bilibili.com/video/BV1be411N7JA/)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/openvpi/DiffSinger/blob/main/LICENSE)

This is a refactored and enhanced version of _DiffSinger: Singing Voice Synthesis via Shallow Diffusion Mechanism_ based on the original [paper](https://arxiv.org/abs/2105.02446) and [implementation](https://github.com/MoonInTheRiver/DiffSinger), which provides:

- Cleaner code structure: useless and redundant files are removed and the others are re-organized.
- Better sound quality: the sampling rate of synthesized audio are adapted to 44.1 kHz instead of the original 24 kHz.
- Higher fidelity: improved acoustic models and diffusion sampling acceleration algorithms are integrated.
- More controllability: introduced variance models and parameters for prediction and control of pitch, energy, breathiness, etc.
- Production compatibility: functionalities are designed to match the requirements of production deployment and the SVS communities.

|                                       Overview                                        |                                    Variance Model                                     |                                    Acoustic Model                                     |
|:-------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| <img src="docs/resources/arch-overview.jpg" alt="arch-overview" style="zoom: 60%;" /> | <img src="docs/resources/arch-variance.jpg" alt="arch-variance" style="zoom: 50%;" /> | <img src="docs/resources/arch-acoustic.jpg" alt="arch-acoustic" style="zoom: 60%;" /> |

## User Guidance

> 中文教程 / Chinese Tutorials: [Text](https://openvpi-docs.feishu.cn/wiki/KmBFwoYDEixrS4kHcTAcajPinPe), [Video](https://space.bilibili.com/179281251/channel/collectiondetail?sid=1747910)

- **Installation & basic usages**: See [Getting Started](docs/GettingStarted.md)
- **Dataset creation pipelines & tools**: See [MakeDiffSinger](https://github.com/openvpi/MakeDiffSinger)
- **Best practices & tutorials**: See [Best Practices](docs/BestPractices.md)
- **Editing configurations**: See [Configuration Schemas](docs/ConfigurationSchemas.md)
- **Deployment & production**: [OpenUTAU for DiffSinger](https://github.com/xunmengshe/OpenUtau), [DiffScope (under development)](https://github.com/SineStriker/qsynthesis-revenge)
- **Communication groups**: [QQ Group](http://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=fibG_dxuPW5maUJwe9_ya5-zFcIwaoOR&authKey=ZgLCG5EqQVUGCID1nfKei8tCnlQHAmD9koxebFXv5WfUchhLwWxb52o1pimNai5A&noverify=0&group_code=907879266) (907879266), [Discord server](https://discord.gg/wwbu2JUMjj)

## Progress & Roadmap

- **Progress since we forked into this repository**: See [Releases](https://github.com/openvpi/DiffSinger/releases)
- **Roadmap for future releases**: See [Project Board](https://github.com/orgs/openvpi/projects/1)
- **Thoughts, proposals & ideas**: See [Discussions](https://github.com/openvpi/DiffSinger/discussions)

## Architecture & Algorithms

TBD

## Development Resources

TBD

## References

- Original DiffSinger: [paper](https://arxiv.org/abs/2105.02446), [implementation](https://github.com/MoonInTheRiver/DiffSinger)
- [HiFi-GAN](https://github.com/jik876/hifi-gan) and [NSF](https://github.com/nii-yamagishilab/project-NN-Pytorch-scripts/tree/master/project/01-nsf) for waveform reconstruction
- [pc-ddsp](https://github.com/yxlllc/pc-ddsp) for waveform reconstruction
- [DDIM](https://arxiv.org/abs/2010.02502) for diffusion sampling acceleration
- [PNDM](https://arxiv.org/abs/2202.09778) for diffusion sampling acceleration
- [DPM-Solver++](https://github.com/LuChengTHU/dpm-solver) for diffusion sampling acceleration
- [UniPC](https://github.com/wl-zhao/UniPC) for diffusion sampling acceleration
- [RMVPE](https://github.com/Dream-High/RMVPE) and yxlllc's [fork](https://github.com/yxlllc/RMVPE) for pitch extraction

## Disclaimer

Any organization or individual is prohibited from using any functionalities included in this repository to generate someone's speech without his/her consent, including but not limited to government leaders, political figures, and celebrities. If you do not comply with this item, you could be in violation of copyright laws.

## License

This forked DiffSinger repository is licensed under the [Apache 2.0 License](LICENSE).

