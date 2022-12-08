#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char* argv[])
{
    // VideoCapture cap("/home/pixel/VikaLabs/1.mp4"); 
    VideoCapture cap(0); 
    if (cap.isOpened() == false) {
        return -1;
    }

    int frame_width = cap.get(CAP_PROP_FRAME_WIDTH);
    int frame_height = cap.get(CAP_PROP_FRAME_HEIGHT);

    VideoWriter ouputVideo("outcpp.avi", cv::VideoWriter::fourcc('M','J','P','G'), 10, Size(frame_width,frame_height));    

    namedWindow("My Video", WINDOW_NORMAL);
    while (true)
    {
        Mat frame;
        cap >> frame;
        if (frame.empty()){
            break;
        }
        ouputVideo.write(frame);
        imshow( "Frame", frame );
        if (waitKey(5) == 27){
            break;
        }
    }
    cap.release();
    ouputVideo.release();
    destroyAllWindows();
    return 0;
}
