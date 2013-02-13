Title: Maple IDE 0.0.10 Released
Date: 2011-05-23 15:52
Author: mbolivar
Category: Uncategorized

That's right, the newest release of the Maple IDE is hot out of the oven, and ready for you to <a href="/docs/maple-ide-install.html">download</a>.

This feature-packed release includes a ton of new stuff; see the <a href="/2011/05/maple-ret6-edition-and-maple-ide-0-0-10-beta/">0.0.10 Beta post</a> for all the juicy details.

Finally, a quick note: there were a few last-minute tweaks we made to the lowest-level layers of <a href="/docs/libmaple.html">libmaple</a> which advanced users of the 0.0.10 Beta may want to take a look at; more after the jump.
<!--more-->

Now that the release is out, the public libmaple APIs are fixed.  This means that every <a href="/docs/libmaple/apis.html">officially documented</a> bit of functionality in libmaple will be present for the foreseeable future, and any changes which break compatibility with these APIs are bugs.  However, we did make a few minor changes in between the time the 0.0.10 beta came out and the final release.

Again, these post-beta changes only affect the very lowest levels of the libmaple, and unless you were messing around down there, they are unlikely to affect you at all. Here's the list:

<ul>
<li>adc.h: adc_init() no longer blindly assumes you want RCC_ADCPRE_PCLK_DIV_6; the caller is responsible for setting the prescaler now, which we do at init() time.</li>
<li>gpio.h: AFIORemapPeripheral was renamed afio_remap_peripheral, and several of its enumerators changed.  The previous definition did not allow for all possible remaps.
</li>
<li><div>i2c.h:  There were a few changes to struct i2c_dev's members:
        <ol><li>"volatile uint8 state" became "volatile i2c_state state"</li>
            <li>"uint8 clk_line" became "rcc_clk_id clk_id"</li>
            <li>"uint8 ev_nvic_line" became "nvic_irq_num ev_nvic_line"</li>
            <li>"uint8 er_nvic_line" became "nvic_irq_num er_nvic_line"</li>
        </ol>
Additionally, i2c_init() was made public.</div>
</li>
<li>rcc.h:The various XXX_prescaler_divider enums used as arguments to rcc_set_prescaler() were badly named.  They have been renamed as follows:
    <ol>
        <li>adc_prescaler_divider became rcc_adc_divider</li>
        <li>apb1_prescaler_divider became rcc_apb1_divider</li>
        <li>apb2_prescaler_divider became rcc_apb2_divider</li>
        <li>ahb_prescaler_divider became rcc_ahb_divider</li>
    </ol>
</li>
<li><div>timer.h: timer_reg_map_union became timer_reg_map.   Additionally, various unbearably long names were shortened:
    <ol>
        <li>timer_enable_interrupt() became timer_enable_irq()</li>
        <li>timer_disable_interrupt() became timer_disable_irq()</li>
        <li>timer_cc_get_polarity() became timer_cc_get_pol()</li>
        <li>timer_cc_set_polarity() became timer_cc_set_pol()</li>
        <li>timer_trigger_dma_enable_request() became timer_dma_enable_trg_req()</li>
        <li>timer_trigger_dma_disable_request() became timer_dma_disable_trg_req()</li>
        <li>timer_dma_enable_request() became timer_dma_enable_req()</li>
        <li>timer_dma_disable_request() became timer_dma_disable_req()</li>
        <li>timer_get_dma_burst_length() became timer_dma_get_burst_len()</li>
        <li>timer_set_dma_burst_length() became timer_dma_set_burst_len()</li>
        <li>timer_get_dma_base_address() became timer_dma_get_base_addr()</li>
        <li>timer_dma_base_address became timer_dma_base_addr</li>
        <li>timer_set_dma_base_address() became timer_dma_set_base_addr()</li>
    </ol>
    </div>
</li>
</ul>
