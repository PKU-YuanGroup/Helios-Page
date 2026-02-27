from moviepy.editor import VideoFileClip

def convert_without_dropping_frames(input_path, output_path, original_fps=30, target_fps=24):
    # 1. 加载视频
    clip = VideoFileClip(input_path)
    
    # 2. 计算速度倍数
    # 为了让原本 30fps 的内容在 24fps 下一帧不差地播放，
    # 我们需要把视频语速/动作放慢到原来的 0.8 倍
    speed_factor = target_fps / original_fps
    
    print(f"正在调整播放速度为: {speed_factor}x (慢动作模式)...")
    
    # 3. 改变播放速度 (这会拉长视频时长)
    # speedx 会自动处理视频帧和音频，保证进度条变长
    new_clip = clip.speedx(speed_factor)
    
    # 4. 写入文件，强制指定输出帧率为 24
    new_clip.write_videofile(output_path, fps=target_fps, codec="libx264")
    
    clip.close()
    print("转换完成！所有原始帧均已保留。")

if __name__ == "__main__":
    convert_without_dropping_frames("checkpoint-10000_2.mp4", "checkpoint-10000_2_24.mp4")