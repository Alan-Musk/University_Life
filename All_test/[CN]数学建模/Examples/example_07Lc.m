function varargout = example_07Lc(varargin)
% EXAMPLE_07LC MATLAB code for example_07Lc.fig
%      EXAMPLE_07LC, by itself, creates a new EXAMPLE_07LC or raises the existing
%      singleton*.
%
%      H = EXAMPLE_07LC returns the handle to a new EXAMPLE_07LC or the handle to
%      the existing singleton*.
%
%      EXAMPLE_07LC('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in EXAMPLE_07LC.M with the given input arguments.
%
%      EXAMPLE_07LC('Property','Value',...) creates a new EXAMPLE_07LC or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before example_07Lc_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to example_07Lc_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help example_07Lc

% Last Modified by GUIDE v2.5 28-Aug-2023 17:15:01

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @example_07Lc_OpeningFcn, ...
                   'gui_OutputFcn',  @example_07Lc_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before example_07Lc is made visible.
function example_07Lc_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to example_07Lc (see VARARGIN)

% Choose default command line output for example_07Lc
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes example_07Lc wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = example_07Lc_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of pushbutton1
handles.peaks=peaks(35);    % 生成一个 35x35 的山峰图
handles.membrane=membrane;  % 创建了一个默认大小的膜状网格
[x,y]=meshgrid(-8:.5:8); r=sqrt(x.^2+y.^2)+eps;
sinc=sin(r)./r; handles.sinc=sinc;
handles.current_data=handles.peaks;
surf(handles.axes1,handles.current_data);