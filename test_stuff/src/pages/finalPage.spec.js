import { describe, it, expect, vi, beforeEach } from 'vitest';
import { mount, flushPromises } from '@vue/test-utils';
import finalPage from './finalPage.vue';

// Mock the API store
vi.mock('@/stores/API', () => ({
  useAPIStore: () => ({ data: { foo: 'bar' } })
}));

// Mock arrowSVG and Basebutton
vi.mock('@/components/icons/buttonArrowFinalPage.vue', () => ({ default: { name: 'arrowSVG', template: '<svg />' } }));
vi.mock('@/components/Basebutton.vue', () => ({ default: { name: 'Basebutton', template: '<button><slot /></button>' } }));

describe('finalPage.vue', () => {
  let fetchMock;

  beforeEach(() => {
    fetchMock = vi.fn();
    global.fetch = fetchMock;
  });

  it('renders loading state by default', async () => {
    fetchMock.mockResolvedValue({ ok: true, blob: async () => new Blob(['test']) });
    const wrapper = mount(finalPage);
    await flushPromises();
    expect(wrapper.text()).toContain('Происходит генерация вашей колоды');
  });

  it('renders ready state after successful fetch', async () => {
    fetchMock.mockResolvedValue({ ok: true, blob: async () => new Blob(['test']) });
    const wrapper = mount(finalPage);
    await flushPromises();
    // Simulate fetch success
    wrapper.vm.isGetResp = true;
    await wrapper.vm.$nextTick();
    expect(wrapper.text()).toContain('Ваша колода готова');
    expect(wrapper.find('.button-csv').exists()).toBe(true);
  });

  it('shows error message on fetch failure', async () => {
    fetchMock.mockResolvedValue({ ok: false, status: 500 });
    const wrapper = mount(finalPage);
    await flushPromises();
    expect(wrapper.text()).toContain('Упс, кажется что-то пошло не так');
    expect(wrapper.vm.isErr).toBe(true);
  });

  it('calls fatchdata on mount', async () => {
    const spy = vi.spyOn(finalPage.methods, 'fatchdata');
    fetchMock.mockResolvedValue({ ok: true, blob: async () => new Blob(['test']) });
    mount(finalPage);
    expect(spy).toHaveBeenCalled();
    spy.mockRestore();
  });

  it('downloadFile triggers download', async () => {
    fetchMock.mockResolvedValue({ ok: true, blob: async () => new Blob(['test']) });
    const wrapper = mount(finalPage);
    await flushPromises();
    wrapper.vm.isGetResp = true;
    wrapper.vm.url = 'blob:http://test';
    document.body.innerHTML = '';
    const clickSpy = vi.spyOn(document.body, 'appendChild');
    wrapper.vm.downloadFile();
    expect(clickSpy).toHaveBeenCalled();
    clickSpy.mockRestore();
  });
}); 