from thinkdsp import CosSignal, SinSignal, decorate, read_wave
import matplotlib.pyplot as plt
wave = read_wave(r'D:\QQ\971mydata\1005470971\FileRecv\dublie_trumpet.wav')
wave.normalize()
wave.make_audio()
wave.plot()
plt.show()
segment = wave.segment(start=1.1, duration=0.3)
segment.make_audio()
segment.plot()
plt.show()
segment.segment(start=1.1, duration=0.005).plot()
spectrum = segment.make_spectrum()
spectrum.plot(high=7000)
plt.show()

spectrum.low_pass(4000)
spectrum.plot(high=7000)
plt.show()

spectrum.high_pass(1000)
spectrum.plot(high=7000)
plt.show()

spectrum.band_stop(2500,1000)
spectrum.plot(high=7000)
plt.show()

# # # 1-3

cos_sig = CosSignal(freq=440,amp=1.0,offset=0)

sin_sig = SinSignal(freq=880,amp=2.0,offset=0)
# # 正弦信号和波形
cos_sig.plot()
decorate(xlabel='Time (s)')
plt.show()
wave1 = cos_sig.make_wave(duration=1)
wave1.apodize()
wave1.make_audio()
spectrum1 = wave1.make_spectrum()
spectrum1.plot(high=2000)
plt.show()
# # # 余弦信号和波形
sin_sig.plot()
decorate(xlabel='Time (s)')
plt.show()
wave2 = cos_sig.make_wave(duration=1)
wave2.apodize()
wave2.make_audio()
spectrum2 = wave2.make_spectrum()
spectrum2.plot(high=2000)
plt.show()
# # # 混合叠加的信号和波形
mix = sin_sig + cos_sig
mix.plot()
decorate(xlabel='Time (s)')
plt.show()
wave3 = mix.make_wave(duration=1)
wave3.apodize()
wave3.make_audio()
spectrum3 = wave3.make_spectrum()
spectrum3.plot(high=2000)
plt.show()

# # 1-4

wave4 = read_wave(r'D:\QQ\971mydata\1005470971\FileRecv\dublie_trumpet.wav')
wave4.normalize()
wave4.make_audio()

def stretch(wave,factor):
    wave.ts *= factor
    wave.framerate /= factor
plt.show()
