import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from mpl_toolkits.axes_grid1 import ImageGrid

image_MoA = pd.read_csv('/Users/emilylorenzen/GitStuff/metis-engineering/image_MoA.csv')

st.title('Help train AI to see what a drug does!')
st.markdown(' ## Analysis of cells imaged treatment with immunological agents')
st.markdown(' ### Can you see how cells treated with drugs that target different protein classes react?')

MoAs = ['GPCR agonist', 'Interleukin', 'Growth Factor', 'Immunoglobulin']

client_response_1  = st.selectbox( 'Which mechanism of action do you want to view in comparison to a negative control?', MoAs)

button = st.button('Ready?')

image_MoA_negative = image_MoA[image_MoA.treatment == 'EMPTY']
df_sample_negative = image_MoA_negative.sample(1)
image_MoA_chosen = image_MoA[image_MoA.mechanism == client_response_1]
df_sample_MoA = image_MoA_chosen.sample(1)

base_dir = '/Users/emilylorenzen/Downloads/rxrx2-2/images/'
negative_image_path = str(base_dir + df_sample_negative['experiment'].item())  + '/Plate' + str(df_sample_negative.plate.item()) + '/' + df_sample_negative.well.item() + '_s' + str(df_sample_negative.site.item())
moa_image_path = str(base_dir + df_sample_MoA['experiment'].item())  + '/Plate' + str(df_sample_MoA.plate.item()) + '/' + df_sample_MoA.well.item() + '_s' + str(df_sample_MoA.site.item())



neg_6_chan_paths = [negative_image_path + '_w' + str(x) + '.png' for x in range(1,7)]
moa_6_chan_paths = [moa_image_path + '_w' + str(x) + '.png' for x in range(1,7)]

image_data = neg_6_chan_paths + moa_6_chan_paths


fig = plt.figure(figsize=(100, 100))
grid = ImageGrid(fig, 261,  # similar to subplot(111)
                 nrows_ncols=(2, 6),  
                 axes_pad=0.1,  # pad between axes in inch.
                 )
i = 0
for ax, im in zip(grid, image_data):
    print(ax)
    im = plt.imread(image_data[i])
    i += 1
    ax.tick_params(top=False, bottom=False, left=False, right=False,
                labelleft=False, labelbottom=False)
    if i >= 7:
        ax.set_xlabel('Channel ' + str(i-6))

    ax.imshow(im)

if button:
    st.pyplot(fig)


st.write('Please select three channels:')
option_1 = st.checkbox('Channel 1')
option_2 = st.checkbox('Channel 2')
option_3 = st.checkbox('Channel 3')
option_4 = st.checkbox('Channel 4')
option_5 = st.checkbox('Channel 5')
option_6 = st.checkbox('Channel 6')
known_variables = option_1 + option_2 + option_3 + option_4 + option_5 + option_6

if known_variables <3:
    st.write('You have to select minimum 3 variables.')
elif known_variables == 3:
    st.write('Thank you for contributing to biomedical research')
elif known_variables >3:
    st.write('You can select maximum 3 variables.')

